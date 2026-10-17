#!/usr/bin/env python3
"""Generate deterministic dataset files from FAQ and guide Markdown pages."""
from __future__ import annotations
import argparse,json,re,sys,unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
OUTPUT_DIR=ROOT/"veri-kumeleri"
SITE_BASE="https://oyuncusempanze.github.io/Oyun-Rehberi/"
FAQ_VERSION="1.0"
GUIDE_VERSION="1.1"
DATASET_VERSION="1.2.0"
GAMES={"bloody-bastards":{"slug":"bloody-bastards","name":"Bloody Bastards"},"DATA-WING":{"slug":"data-wing","name":"DATA WING"},"wplace.live":{"slug":"wplace-live","name":"Wplace.live"}}
ORDER={"bloody-bastards":0,"DATA-WING":1,"wplace.live":2}
LABELS={"Resmî Kaynak":"official_source","Oyun İçi Gözlem":"in_game_observation","Kaynak":"reference_source","Öneri":"recommendation"}
LABEL_RE=re.compile(r"\[(Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\]")
LINK_RE=re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
ANY_LINK_RE=re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")
IMAGE_RE=re.compile(r"!\[[^\]]*\]\([^)]+\)")
SECTION_RE=re.compile(r"(?m)^##\s+(.+?)\s*$")
FRONT_RE=re.compile(r"\A---\s*\n([\s\S]*?)\n---\s*\n?")
QUESTION_OVERRIDES={
("bloody-bastards","İlerleme ve seviye sistemi"):"Oyunda ilerleme ve seviye sistemi nasıl çalışıyor?",
("bloody-bastards","Türkçe dil desteği"):"Oyunda Türkçe dil desteği var mı?",
("bloody-bastards","Çok oyunculu eşleştirme ve sürüm koşulları"):"Çok oyunculu eşleştirme ve sürüm koşulları nasıl işliyor?",
("wplace.live","Türkçe arayüz desteği"):"Oyunda Türkçe arayüz desteği var mı?"
}
COMMON={"id","language","game","game_slug","record_type","evidence_types","sources","content_url","license","schema_version"}

def slugify(value:str)->str:
    value=value.lower().replace("ı","i")
    value=unicodedata.normalize("NFKD",value)
    value="".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+","-",value).strip("-")

def plain_text(md:str)->str:
    text=IMAGE_RE.sub("",md)
    text=re.sub(r"\[(?:Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\](?:\([^)]*\))?","",text)
    text=ANY_LINK_RE.sub(r"\1",text)
    text=re.sub(r"(?m)^\s{0,3}#{1,6}\s+","",text)
    text=re.sub(r"(?m)^\s*[-*+]\s+","",text)
    text=re.sub(r"(?m)^\s*\d+[.)]\s+","",text)
    text=re.sub(r"(\*\*|__)(.*?)\1",r"\2",text,flags=re.DOTALL)
    text=re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)",r"\1",text)
    text=re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)",r"\1",text)
    text=re.sub(chr(96)+r"([^"+chr(96)+r"]+)"+chr(96),r"\1",text)
    return " ".join(text.split()).strip()

def game_for(path:Path)->dict[str,str]:
    folder=path.parent.name
    return GAMES.get(folder,{"slug":slugify(folder),"name":folder.replace("-"," ").replace("."," ").title()})

def extract_links(md:str,path:Path)->list[dict[str,str]]:
    # Only external links are evidence sources. Internal navigation links remain in the
    # Markdown content and are not mislabeled as independent references.
    links=[];seen=set()
    for m in LINK_RE.finditer(md):
        label,url=m.groups()
        key=(label.strip(),url)
        if key not in seen:links.append({"label":key[0],"url":url});seen.add(key)
    return links

def evidence_types(md:str,links:list[dict[str,str]])->list[str]:
    found=[]
    for m in LABEL_RE.finditer(md):
        value=LABELS[m.group(1)]
        if value not in found:found.append(value)
    for link in links:
        label=link["label"].casefold()
        value="official_source" if ("resmî" in label or "resmi" in label) else ("reference_source" if any(w in label for w in ("kaynak","source","topluluk")) else None)
        if value and value not in found:found.append(value)
    return found

def read_meta(md:str)->tuple[dict[str,str],str]:
    m=FRONT_RE.match(md)
    if not m:return {},md
    meta={}
    for line in m.group(1).splitlines():
        row=re.match(r"^([\w-]+):\s*(.*)$",line)
        if row:meta[row.group(1)]=row.group(2).strip().strip("\"'")
    return meta,md[m.end():]

def base_record(path:Path,kind:str,version:str)->dict[str,Any]:
    g=game_for(path)
    return {"id":"","language":"tr","game":g["name"],"game_slug":g["slug"],"record_type":kind}

def content_url_for(path:Path)->str:
    relative=path.relative_to(ROOT).with_suffix("").as_posix()
    return f"{SITE_BASE}{relative}/"

def faq_question(folder:str,heading:str)->str|None:
    if "?" in heading or "？" in heading:return heading
    return QUESTION_OVERRIDES.get((folder,heading))

def extract_faq(path:Path)->list[dict[str,Any]]:
    md=path.read_text(encoding="utf-8");matches=list(SECTION_RE.finditer(md));out=[]
    for i,m in enumerate(matches):
        heading=m.group(1).strip();end=matches[i+1].start() if i+1<len(matches) else len(md)
        answer_md=md[m.end():end].strip();question=faq_question(path.parent.name,heading)
        if not question or not plain_text(answer_md):continue
        links=extract_links(answer_md,path);record=base_record(path,"faq",FAQ_VERSION)
        record.update({"id":f"{record['game_slug']}-{slugify(question)}","question":question,"answer":plain_text(answer_md),"answer_markdown":answer_md,"evidence_types":evidence_types(answer_md,links),"sources":links,"content_url":content_url_for(path),"license":"CC-BY-4.0","schema_version":FAQ_VERSION})
        out.append(record)
    return out

def extract_guides(path:Path)->list[dict[str,Any]]:
    md=path.read_text(encoding="utf-8");meta,body=read_meta(md)
    body=re.sub(r"(?m)^\s*#\s+.+?\n+","",body,count=1).strip()
    matches=list(SECTION_RE.finditer(body));sections=[]
    if matches:
        intro=body[:matches[0].start()].strip()
        if len(plain_text(intro))>=50:sections.append(("Giriş",intro))
        for i,m in enumerate(matches):
            title=m.group(1).strip()
            if title.casefold() in {"kaynak","kaynaklar","sources","görseller"}:continue
            end=matches[i+1].start() if i+1<len(matches) else len(body)
            section=body[m.end():end].strip()
            if len(plain_text(section))>=30:sections.append((title,section))
    elif len(plain_text(body))>=30:sections.append(("Genel bakış",body))
    article_title=meta.get("title") or path.stem;out=[]
    for title,raw in sections:
        section_md=IMAGE_RE.sub("",raw).strip();content=plain_text(section_md)
        if not content:continue
        links=extract_links(section_md,path);record=base_record(path,"guide_section",GUIDE_VERSION)
        record.update({"id":f"{record['game_slug']}-{slugify(path.stem)}-{slugify(title)}","article_title":article_title,"section_title":title,"content":content,"content_markdown":section_md,"evidence_types":evidence_types(section_md,links),"sources":links,"content_url":content_url_for(path),"license":"CC-BY-4.0","schema_version":GUIDE_VERSION})
        out.append(record)
    return out

def jsonl(records:list[dict[str,Any]])->str:
    return "".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in records)

def validate(records:list[dict[str,Any]])->None:
    ids=set()
    for r in records:
        missing=COMMON-r.keys()
        if missing:raise ValueError(f"{r.get('id','?')}: missing {sorted(missing)}")
        if r["id"] in ids:raise ValueError(f"duplicate record ID: {r['id']}")
        ids.add(r["id"])
        if r["record_type"]=="faq":required={"question","answer","answer_markdown"};text_fields=("question","answer")
        elif r["record_type"]=="guide_section":required={"article_title","section_title","content","content_markdown"};text_fields=("article_title","section_title","content")
        else:raise ValueError(f"unknown record type: {r['record_type']}")
        if required-r.keys():raise ValueError(f"{r['id']}: missing {sorted(required-r.keys())}")
        if any(not r[k].strip() for k in text_fields):raise ValueError(f"{r['id']}: empty text field")
        if not isinstance(r["evidence_types"],list) or any(x not in LABELS.values() for x in r["evidence_types"]):
            raise ValueError(f"{r['id']}: invalid evidence_types")
        if not r["evidence_types"]:
            raise ValueError(f"{r['id']}: evidence_types must not be empty")
        if not isinstance(r["sources"],list):
            raise ValueError(f"{r['id']}: sources must be a list")
        for source in r["sources"]:
            if not isinstance(source,dict) or not isinstance(source.get("label"),str) or not isinstance(source.get("url"),str):
                raise ValueError(f"{r['id']}: malformed source entry")
            parsed=urlparse(source["url"])
            if parsed.scheme not in {"https","http"} or not parsed.netloc:
                raise ValueError(f"{r['id']}: source URL must be an absolute HTTP(S) URL")
        parsed_content=urlparse(r["content_url"])
        if parsed_content.scheme not in {"https","http"} or not parsed_content.netloc:
            raise ValueError(f"{r['id']}: content_url must be an absolute HTTP(S) URL")

def build_outputs()->dict[str,str]:
    faq_paths=sorted(ROOT.glob("oyunlar/*/sik-sorulan-sorular.md"),key=lambda p:(ORDER.get(p.parent.name,99),p.as_posix()))
    if not faq_paths:raise ValueError("No FAQ Markdown pages were found.")
    faq_by_game={};faqs=[]
    for p in faq_paths:
        rows=extract_faq(p)
        if rows:faq_by_game.setdefault(game_for(p)["slug"],[]).extend(rows);faqs.extend(rows)
    guide_paths=sorted((p for p in ROOT.glob("oyunlar/*/*.md") if p.name not in {"index.md","sik-sorulan-sorular.md","gorseller.md"}),key=lambda p:(ORDER.get(p.parent.name,99),p.as_posix()))
    guide_by_game={};guides=[]
    for p in guide_paths:
        rows=extract_guides(p)
        if rows:guide_by_game.setdefault(game_for(p)["slug"],[]).extend(rows);guides.extend(rows)
    all_records=faqs+guides;validate(all_records)
    outputs={"oyun-rehberi-sss-v1.jsonl":jsonl(faqs),"oyun-rehberi-rehber-bolumleri-v1.jsonl":jsonl(guides),"oyun-rehberi-tam-arsiv-v1.jsonl":jsonl(all_records)}
    game_slugs=list(dict.fromkeys(r["game_slug"] for r in all_records))
    for slug in game_slugs:
        game_records=[r for r in all_records if r["game_slug"]==slug]
        outputs[f"{slug}-tam-arsiv-v1.jsonl"]=jsonl(game_records)
    for slug,rows in faq_by_game.items():outputs[f"{slug}-sss-v1.jsonl"]=jsonl(rows)
    file_entries=[{"path":"oyun-rehberi-tam-arsiv-v1.jsonl","scope":"all_records","format":"jsonl","records":len(all_records)},{"path":"oyun-rehberi-rehber-bolumleri-v1.jsonl","scope":"guide_sections","format":"jsonl","records":len(guides)},{"path":"oyun-rehberi-sss-v1.jsonl","scope":"faq","format":"jsonl","records":len(faqs)}]
    for slug in game_slugs:
        game_records=[r for r in all_records if r["game_slug"]==slug]
        name=next((r["game"] for r in all_records if r["game_slug"]==slug),slug)
        file_entries.append({"path":f"{slug}-tam-arsiv-v1.jsonl","scope":"game_archive","game":name,"game_slug":slug,"format":"jsonl","records":len(game_records)})
    for slug,rows in faq_by_game.items():
        name=next((g["name"] for g in GAMES.values() if g["slug"]==slug),slug)
        file_entries.append({"path":f"{slug}-sss-v1.jsonl","scope":"game_faq","game":name,"game_slug":slug,"format":"jsonl","records":len(rows)})
    manifest={"name":"Oyun-Rehberi Türkçe Oyun Bilgisi Veri Kümesi","dataset_version":DATASET_VERSION,"schema_version":"1.1","language":"tr","format":"JSON Lines (UTF-8), one JSON object per line","license":"CC-BY-4.0","source_repository":"https://github.com/OyuncuSempanze/Oyun-Rehberi","website":SITE_BASE,"description":"SSS kayıtları ile mekanikler, oynanış, kurallar, güncellemeler ve diğer rehber bölümlerini içeren Türkçe oyun bilgisi arşivi.","record_count":len(all_records),"collections":[{"record_type":"faq","records":len(faqs),"description":"Soru-cevap biçimindeki sık sorulan sorular."},{"record_type":"guide_section","records":len(guides),"description":"Rehber belgelerindeki anlamlı bölümler."}],"source_files":[p.relative_to(ROOT).as_posix() for p in faq_paths+guide_paths],"files":file_entries,"schema_url":f"{SITE_BASE}veri-kumeleri/schema-v1.json","rights_notice":"CC BY 4.0 yalnızca arşivin lisanslama yetkisine sahip olduğu özgün metin ve düzenleme unsurlarına uygulanır. Kaynak bağlantıları ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir.","limitations":["Guide-section records preserve meaningful document sections; they are not guaranteed to be atomic single claims.","This dataset is a starting point for retrieval and evaluation, not a claim of readiness for every model-training task.","Source links identify references but do not independently prove that each claim is correct."]}
    outputs["manifest.json"]=json.dumps(manifest,ensure_ascii=False,indent=2)+"\n"
    return outputs

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--check",action="store_true",help="check exports against source Markdown");args=parser.parse_args()
    try:outputs=build_outputs()
    except (OSError,ValueError,json.JSONDecodeError) as error:print(f"Dataset error: {error}",file=sys.stderr);return 1
    if args.check:
        stale=[]
        for filename,expected in outputs.items():
            path=OUTPUT_DIR/filename
            if not path.is_file():
                stale.append(filename)
                continue
            actual_text=path.read_text(encoding="utf-8")
            if filename.endswith(".jsonl"):
                try:
                    expected_rows=[json.loads(line) for line in expected.splitlines() if line.strip()]
                    actual_rows=[json.loads(line) for line in actual_text.splitlines() if line.strip()]
                except json.JSONDecodeError:
                    stale.append(filename)
                    print(f"Invalid JSONL in {filename}.",file=sys.stderr)
                    continue
                if actual_rows!=expected_rows:
                    stale.append(filename)
                    for index,(actual_row,expected_row) in enumerate(zip(actual_rows,expected_rows),start=1):
                        if actual_row!=expected_row:
                            changed=[key for key in set(actual_row)|set(expected_row) if actual_row.get(key)!=expected_row.get(key)]
                            print(f"{filename}:{index}: record {expected_row.get('id',actual_row.get('id','?'))} differs in {sorted(changed)}.",file=sys.stderr)
                            break
                    if len(actual_rows)!=len(expected_rows):
                        print(f"{filename}: expected {len(expected_rows)} records, found {len(actual_rows)}.",file=sys.stderr)
            elif filename.endswith(".json"):
                try:
                    if json.loads(actual_text)!=json.loads(expected):
                        stale.append(filename)
                except json.JSONDecodeError:
                    stale.append(filename)
            elif actual_text!=expected:
                stale.append(filename)
        wanted={x for x in outputs if x.endswith(".jsonl")}
        if OUTPUT_DIR.exists():
            for path in OUTPUT_DIR.glob("*.jsonl"):
                if path.name not in wanted:stale.append(path.name+" (stale file)")
        if stale:
            print("Generated dataset files are out of date. Run python scripts/build_dataset.py.",file=sys.stderr)
            for name in sorted(set(stale)):print(f"- {name}",file=sys.stderr)
            return 1
        print(f"Dataset check passed: {len(outputs['oyun-rehberi-tam-arsiv-v1.jsonl'].splitlines())} records.");return 0
    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
    for name,content in outputs.items():(OUTPUT_DIR/name).write_text(content,encoding="utf-8",newline="\n")
    print(f"Generated {len(outputs)} files and {len(outputs['oyun-rehberi-tam-arsiv-v1.jsonl'].splitlines())} records.")
    return 0
if __name__=="__main__":raise SystemExit(main())
