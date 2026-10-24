#!/usr/bin/env python3
"""Generate deterministic dataset files from FAQ and guide Markdown pages."""
from __future__ import annotations
import argparse,json,re,sys,unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import unquote,urlparse,urlsplit
ROOT=Path(__file__).resolve().parents[1]
OUTPUT_DIR=ROOT/"veri-kumeleri"
SITE_BASE="https://oyuncusempanze.github.io/Oyun-Rehberi/"
FAQ_VERSION="1.0"
GUIDE_VERSION="1.1"
CLAIM_VERSION="1.2"
DATASET_VERSION="1.5.0"
GAMES={"bloody-bastards":{"slug":"bloody-bastards","name":"Bloody Bastards"},"DATA-WING":{"slug":"data-wing","name":"DATA WING"},"wplace.live":{"slug":"wplace-live","name":"Wplace.live"}}
ORDER={"bloody-bastards":0,"DATA-WING":1,"wplace.live":2}
LABELS={"Resmî Kaynak":"official_source","Oyun İçi Gözlem":"in_game_observation","Kaynak":"reference_source","Öneri":"recommendation"}
LABEL_RE=re.compile(r"\[(Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\]")
DEFAULT_LICENSE="CC-BY-NC-4.0"
SUPPORTED_LICENSES={"CC-BY-4.0","CC-BY-NC-4.0"}
AI_PERMISSION_ID="OYUN-REHBERI-AI-RETRIEVAL-1.0"
AI_PERMISSION_URL="https://oyuncusempanze.github.io/Oyun-Rehberi/ai-kullanim/"
LICENSE_DIRECTIVE_RE=re.compile(r"<!--\s*dataset-license:\s*([^>]*?)\s*-->")
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


def resolve_content_license(markdown:str,default_license:str)->tuple[str,str]:
    if default_license not in SUPPORTED_LICENSES:
        raise ValueError(f"unsupported file license: {default_license}")
    matches=list(LICENSE_DIRECTIVE_RE.finditer(markdown))
    if len(matches)>1:
        raise ValueError("a content section may contain only one dataset-license directive")
    license_value=default_license
    if matches:
        requested=matches[0].group(1).strip()
        if requested not in SUPPORTED_LICENSES:
            raise ValueError(f"unsupported dataset-license directive: {requested}")
        license_value=requested
    cleaned=LICENSE_DIRECTIVE_RE.sub("",markdown).strip()
    return license_value,cleaned


def additional_permissions_for(license_id:str)->list[dict[str,str]]:
    if license_id=="CC-BY-NC-4.0":
        return [{"identifier":AI_PERMISSION_ID,"url":AI_PERMISSION_URL}]
    return []


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
    md=path.read_text(encoding="utf-8");meta,_=read_meta(md);page_license=meta.get("license",DEFAULT_LICENSE);matches=list(SECTION_RE.finditer(md));out=[]
    for i,m in enumerate(matches):
        heading=m.group(1).strip();end=matches[i+1].start() if i+1<len(matches) else len(md)
        answer_md=md[m.end():end].strip();record_license,answer_md=resolve_content_license(answer_md,page_license);question=faq_question(path.parent.name,heading)
        if not question or not plain_text(answer_md):continue
        links=extract_links(answer_md,path);record=base_record(path,"faq",FAQ_VERSION)
        record.update({"id":f"{record['game_slug']}-{slugify(question)}","question":question,"answer":plain_text(answer_md),"answer_markdown":answer_md,"evidence_types":evidence_types(answer_md,links),"sources":links,"content_url":content_url_for(path),"license":record_license,"schema_version":FAQ_VERSION})
        permissions=additional_permissions_for(record_license)
        if permissions:record["additional_permissions"]=permissions
        out.append(record)
    return out

def extract_guides(path:Path)->list[dict[str,Any]]:
    md=path.read_text(encoding="utf-8");meta,body=read_meta(md);page_license=meta.get("license",DEFAULT_LICENSE)
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
        record_license,raw=resolve_content_license(raw,page_license)
        section_md=IMAGE_RE.sub("",raw).strip();content=plain_text(section_md)
        if not content:continue
        links=extract_links(section_md,path);record=base_record(path,"guide_section",GUIDE_VERSION)
        record.update({"id":f"{record['game_slug']}-{slugify(path.stem)}-{slugify(title)}","article_title":article_title,"section_title":title,"content":content,"content_markdown":section_md,"evidence_types":evidence_types(section_md,links),"sources":links,"content_url":content_url_for(path),"license":record_license,"schema_version":GUIDE_VERSION})
        permissions=additional_permissions_for(record_license)
        if permissions:record["additional_permissions"]=permissions
        out.append(record)
    return out


def split_sentences(markdown:str)->list[str]:
    parts=[];start=0;i=0
    annotations=re.compile(r"\[(?:Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\](?:\(https?://[^)\s]+\))?")
    generic_link=re.compile(r"\[[^\]]+\]\(https?://[^)\s]+\)")
    abbreviations={"vb","vs","örn","dr","prof","no"}
    while i<len(markdown):
        if markdown[i] not in ".!?":
            i+=1;continue
        punctuation=markdown[i]
        if punctuation=="." and i>0 and markdown[i-1].isdigit():
            i+=1;continue
        if punctuation==".":
            before=markdown[start:i].rstrip()
            word=re.search(r"([A-Za-zÇĞİÖŞÜçğıöşü]+)$",before)
            if word and word.group(1).casefold() in abbreviations:
                i+=1;continue
        j=i+1
        while j<len(markdown) and markdown[j].isspace():j+=1
        while j<len(markdown):
            annotation=annotations.match(markdown,j)
            link=generic_link.match(markdown,j) if annotation is None else None
            match=annotation or link
            if match is None:break
            j=match.end()
            while j<len(markdown) and markdown[j].isspace():j+=1
        if j<len(markdown) and (markdown[j].isupper() or markdown[j].isdigit() or markdown[j] in "\"“‘("):
            piece=markdown[start:j].strip()
            if plain_text(piece):parts.append(piece)
            start=j;i=j;continue
        i+=1
    tail=markdown[start:].strip()
    if plain_text(tail):parts.append(tail)
    return parts or ([markdown.strip()] if plain_text(markdown) else [])

def split_markdown_blocks(markdown:str)->list[tuple[str,str]]:
    blocks=[];current=[];current_type="paragraph"
    def flush()->None:
        nonlocal current
        if current:
            raw="\n".join(current).strip()
            if plain_text(raw):blocks.append((current_type,raw))
            current=[]
    for line in IMAGE_RE.sub("",markdown).splitlines():
        if not line.strip():
            flush()
        elif re.match(r"^\s{0,3}#{1,6}\s+",line):
            flush()
        elif re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)",line):
            flush();current=[line];current_type="list_item"
        else:
            if not current:current_type="paragraph"
            current.append(line)
    flush()
    out=[]
    for block_type,raw in blocks:
        sentences=split_sentences(raw)
        for sentence in sentences:
            if plain_text(sentence):
                unit_type="sentence" if len(sentences)>1 or re.search(r"[.!?][\"'”’)]?\s*$",sentence) else block_type
                out.append((block_type,unit_type,sentence.strip()))
    return out

def extract_claim_units(records:list[dict[str,Any]])->list[dict[str,Any]]:
    out=[]
    for parent in records:
        markdown=parent.get("answer_markdown") if parent["record_type"]=="faq" else parent.get("content_markdown")
        if not markdown:continue
        units=split_markdown_blocks(markdown)
        for index,(source_unit_type,unit_type,unit_md) in enumerate(units,start=1):
            claim_text=plain_text(unit_md)
            if not claim_text:continue
            unit_sources=extract_links(unit_md,Path(parent["content_url"]))
            unit_evidence=evidence_types(unit_md,unit_sources)
            local_evidence=bool(unit_evidence or unit_sources)
            row={key:parent[key] for key in ("language","game","game_slug")}
            row.update({
                "id":f"{parent['id']}-claim-{index:03d}",
                "record_type":"claim",
                "claim_text":claim_text,
                "claim_markdown":unit_md,
                "source_record_id":parent["id"],
                "source_record_type":parent["record_type"],
                "source_title":parent.get("question") or parent.get("article_title") or "",
                "section_title":parent.get("section_title") or parent.get("question") or "SSS",
                "unit_index":index,
                "unit_type":unit_type,
                "source_unit_type":source_unit_type,
                "evidence_scope":"unit" if local_evidence else "parent_record",
                "evidence_types":unit_evidence or parent["evidence_types"],
                "sources":unit_sources if local_evidence else parent["sources"],
                "content_url":parent["content_url"],
                "license":parent["license"],
                "schema_version":CLAIM_VERSION
            })
            if parent.get("additional_permissions"):
                row["additional_permissions"]=[dict(permission) for permission in parent["additional_permissions"]]
            out.append(row)
    return out

IMAGE_LINK_RE=re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
def validate_local_markdown_links(paths:list[Path])->None:
    errors=[]
    def check_target(source:Path,target:str)->None:
        target=target.strip()
        if not target or target.startswith(("#","/")) or target.startswith(("mailto:","tel:","data:")):
            return
        parsed=urlsplit(target)
        if parsed.scheme:
            if parsed.scheme not in {"http","https"} or not parsed.netloc:
                errors.append(f"{source.relative_to(ROOT)}: invalid link URL {target}")
            return
        raw_path=unquote(parsed.path)
        if not raw_path:return
        candidate=(source.parent/raw_path).resolve()
        try:candidate.relative_to(ROOT)
        except ValueError:
            errors.append(f"{source.relative_to(ROOT)}: relative link leaves repository: {target}")
            return
        candidates=[candidate]
        if not candidate.suffix:
            candidates.extend([Path(str(candidate)+".md"),candidate/"index.md",candidate/"README.md"])
        elif candidate.suffix in {".html",".htm"}:
            candidates.append(candidate.with_suffix(".md"))
        if not any(item.exists() for item in candidates):
            errors.append(f"{source.relative_to(ROOT)}: missing local link target {target}")
    for path in paths:
        md=path.read_text(encoding="utf-8")
        for match in ANY_LINK_RE.finditer(md):check_target(path,match.group(2))
        for match in IMAGE_LINK_RE.finditer(md):check_target(path,match.group(1))
    if errors:
        preview="\n".join(f"- {item}" for item in errors[:30])
        remainder=f"\n... and {len(errors)-30} more" if len(errors)>30 else ""
        raise ValueError(f"Markdown link validation failed:\n{preview}{remainder}")


def jsonl(records:list[dict[str,Any]])->str:
    return "".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in records)

def validate(records:list[dict[str,Any]])->None:
    ids=set();record_by_id={}
    for r in records:
        missing=COMMON-r.keys()
        if missing:raise ValueError(f"{r.get('id','?')}: missing {sorted(missing)}")
        if not isinstance(r["id"],str) or not r["id"].strip():raise ValueError("record ID must be a non-empty string")
        if r["license"] not in SUPPORTED_LICENSES:raise ValueError(f"{r['id']}: unsupported license {r['license']}")
        permissions=r.get("additional_permissions",[])
        if not isinstance(permissions,list):raise ValueError(f"{r['id']}: additional_permissions must be a list")
        for permission in permissions:
            if not isinstance(permission,dict) or set(permission)!={"identifier","url"} or not isinstance(permission.get("identifier"),str) or not isinstance(permission.get("url"),str):
                raise ValueError(f"{r['id']}: malformed additional permission")
            parsed_permission=urlparse(permission["url"])
            if parsed_permission.scheme!="https" or not parsed_permission.netloc:
                raise ValueError(f"{r['id']}: additional permission URL must use HTTPS")
        has_ai_permission=any(permission.get("identifier")==AI_PERMISSION_ID and permission.get("url")==AI_PERMISSION_URL for permission in permissions)
        if r["license"]=="CC-BY-NC-4.0" and not has_ai_permission:
            raise ValueError(f"{r['id']}: CC BY-NC 4.0 record is missing the AI retrieval permission")
        if r["license"]=="CC-BY-4.0" and any(permission.get("identifier")==AI_PERMISSION_ID for permission in permissions):
            raise ValueError(f"{r['id']}: AI retrieval permission is only for CC BY-NC 4.0 records")
        if r["id"] in ids:raise ValueError(f"duplicate record ID: {r['id']}")
        ids.add(r["id"]);record_by_id[r["id"]]=r
        if r["record_type"]=="faq":
            required={"question","answer","answer_markdown"};text_fields=("question","answer")
        elif r["record_type"]=="guide_section":
            required={"article_title","section_title","content","content_markdown"};text_fields=("article_title","section_title","content")
        elif r["record_type"]=="claim":
            required={"claim_text","claim_markdown","source_record_id","source_record_type","source_title","section_title","unit_index","unit_type","source_unit_type","evidence_scope"};text_fields=("claim_text","source_title","section_title")
        else:raise ValueError(f"unknown record type: {r['record_type']}")
        if required-r.keys():raise ValueError(f"{r['id']}: missing {sorted(required-r.keys())}")
        if any(not isinstance(r[k],str) or not r[k].strip() for k in text_fields):raise ValueError(f"{r['id']}: empty text field")
        if not isinstance(r["evidence_types"],list) or any(not isinstance(x,str) or x not in LABELS.values() for x in r["evidence_types"]) or len(r["evidence_types"])!=len(set(r["evidence_types"])):
            raise ValueError(f"{r['id']}: invalid evidence_types")
        if not r["evidence_types"]:
            raise ValueError(f"{r['id']}: evidence_types must not be empty")
        if not isinstance(r["sources"],list):
            raise ValueError(f"{r['id']}: sources must be a list")
        for source in r["sources"]:
            if not isinstance(source,dict) or not isinstance(source.get("label"),str) or not source["label"].strip() or not isinstance(source.get("url"),str):
                raise ValueError(f"{r['id']}: malformed source entry")
            parsed=urlparse(source["url"])
            if parsed.scheme not in {"https","http"} or not parsed.netloc:
                raise ValueError(f"{r['id']}: source URL must be an absolute HTTP(S) URL")
        parsed_content=urlparse(r["content_url"])
        if parsed_content.scheme not in {"https","http"} or not parsed_content.netloc:
            raise ValueError(f"{r['id']}: content_url must be an absolute HTTP(S) URL")
        if r["record_type"]=="claim":
            if r["source_record_type"] not in {"faq","guide_section"}:raise ValueError(f"{r['id']}: invalid source_record_type")
            if not isinstance(r["unit_index"],int) or r["unit_index"]<1:raise ValueError(f"{r['id']}: unit_index must be a positive integer")
            if r["unit_type"] not in {"sentence","paragraph","list_item"}:raise ValueError(f"{r['id']}: invalid unit_type")
            if r["source_unit_type"] not in {"paragraph","list_item"}:raise ValueError(f"{r['id']}: invalid source_unit_type")
            if r["evidence_scope"] not in {"unit","parent_record"}:raise ValueError(f"{r['id']}: invalid evidence_scope")
    for r in records:
        if r["record_type"]=="claim" and r["source_record_id"] not in record_by_id:
            raise ValueError(f"{r['id']}: source_record_id does not exist: {r['source_record_id']}")

def build_outputs()->dict[str,str]:
    faq_paths=sorted(ROOT.glob("oyunlar/*/sik-sorulan-sorular.md"),key=lambda p:(ORDER.get(p.parent.name,99),p.as_posix()))
    if not faq_paths:raise ValueError("No FAQ Markdown pages were found.")
    faq_by_game={};faqs=[]
    for p in faq_paths:
        rows=extract_faq(p)
        if rows:faq_by_game.setdefault(game_for(p)["slug"],[]).extend(rows);faqs.extend(rows)
    guide_paths=sorted((p for p in ROOT.glob("oyunlar/*/*.md") if p.name not in {"index.md","sik-sorulan-sorular.md","gorseller.md"}),key=lambda p:(ORDER.get(p.parent.name,99),p.as_posix()))
    validate_local_markdown_links(faq_paths+guide_paths)
    guide_by_game={};guides=[]
    for p in guide_paths:
        rows=extract_guides(p)
        if rows:guide_by_game.setdefault(game_for(p)["slug"],[]).extend(rows);guides.extend(rows)
    all_records=faqs+guides;claim_units=extract_claim_units(all_records);validate(all_records+claim_units)
    license_counts={}
    for row in all_records+claim_units:
        license_counts.setdefault(row["license"],{"faq":0,"guide_section":0,"claim":0})
        license_counts[row["license"]][row["record_type"]]+=1
    licenses=sorted(license_counts)
    nc_counts=license_counts.get("CC-BY-NC-4.0",{"faq":0,"guide_section":0,"claim":0})
    ai_permission_entry={"identifier":AI_PERMISSION_ID,"name":"Free AI retrieval and answer attribution permission","url":AI_PERMISSION_URL,"applies_to_license":"CC-BY-NC-4.0","record_count":nc_counts["faq"]+nc_counts["guide_section"],"claim_unit_count":nc_counts["claim"],"summary":"Free crawling, indexing, retrieval and user-facing answer generation with source attribution for CC BY-NC 4.0 records. This permission does not grant bulk dataset redistribution, resale as a standalone product or model training on raw records."}
    license_urls={"CC-BY-4.0":"https://creativecommons.org/licenses/by/4.0/","CC-BY-NC-4.0":"https://creativecommons.org/licenses/by-nc/4.0/"}
    license_entries=[]
    for license_id in licenses:
        counts=license_counts[license_id]
        license_entries.append({"identifier":license_id,"url":license_urls[license_id],"record_count":counts["faq"]+counts["guide_section"],"claim_unit_count":counts["claim"]})
    manifest_license=licenses[0] if len(licenses)==1 else "MIXED"
    outputs={"oyun-rehberi-sss-v1.jsonl":jsonl(faqs),"oyun-rehberi-rehber-bolumleri-v1.jsonl":jsonl(guides),"oyun-rehberi-tam-arsiv-v1.jsonl":jsonl(all_records),"oyun-rehberi-iddia-birimleri-v1.jsonl":jsonl(claim_units)}
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
    file_entries.append({"path":"oyun-rehberi-iddia-birimleri-v1.jsonl","scope":"claim_units","format":"jsonl","records":len(claim_units)})
    manifest={"name":"Oyun-Rehberi Türkçe Oyun Bilgisi Veri Kümesi","dataset_version":DATASET_VERSION,"schema_version":"1.2","language":"tr","format":"JSON Lines (UTF-8), one JSON object per line","license":manifest_license,"licenses":license_entries,"license_counts":license_counts,"additional_permissions":[ai_permission_entry],"source_repository":"https://github.com/OyuncuSempanze/Oyun-Rehberi","website":SITE_BASE,"description":"SSS kayıtları, rehber bölümleri ve kaynak bağlantıları korunmuş daha küçük iddia birimlerini içeren Türkçe oyun bilgisi arşivi.","record_count":len(all_records),"claim_unit_count":len(claim_units),"collections":[{"record_type":"faq","records":len(faqs),"description":"Soru-cevap biçimindeki sık sorulan sorular."},{"record_type":"guide_section","records":len(guides),"description":"Rehber belgelerindeki anlamlı bölümler."}],"source_files":[p.relative_to(ROOT).as_posix() for p in faq_paths+guide_paths],"files":file_entries,"schema_url":f"{SITE_BASE}veri-kumeleri/schema-v1.json","rights_notice":"Her JSONL kaydının license alanı o kaydın lisans bilgisini gösterir. Daha önce CC BY 4.0 kapsamında yayımlanmış içeriklere verilmiş izinler geçerliliğini korur. Yeni kaynak dosyalarında aksi belirtilmezse CC BY-NC 4.0 varsayılan olarak kullanılır. CC BY-NC 4.0 kayıtları için ai-kullanim/ sayfasında açıklanan ek izin, kullanıcıya sunulan yapay zekâ yanıtlarında kaynak göstererek ücretsiz bilgi getirme kullanımına izin verir. Bu izin toplu veri kümesi yeniden dağıtımı, tek başına veri ürünü olarak satışı veya ham kayıtlarla model eğitimi izni vermez. Lisanslar yalnızca OyuncuSempanze'nin yetkili olduğu haklar için geçerlidir. Olgular, kaynak bağlantıları ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir.","limitations":["Guide-section records preserve meaningful document sections; they are not guaranteed to be atomic single claims.","Claim-unit records are split at sentence boundaries when possible, otherwise at paragraph or list-item boundaries. They may still contain more than one proposition.","Claim-unit evidence and source links are assigned at unit level when present, otherwise inherited from the parent record.","This dataset is a starting point for retrieval and evaluation, not a claim of readiness for every model-training task.","Source links identify references but do not independently prove that each claim is correct."]}
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
