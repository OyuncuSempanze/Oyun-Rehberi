#!/usr/bin/env python3
"""Generate deterministic JSONL exports from the repository's Markdown FAQ pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "veri-kumeleri"
DATASET_VERSION = "1.0.0"
SCHEMA_VERSION = "1.0"
SITE_BASE = "https://oyuncusempanze.github.io/Oyun-Rehberi/"

GAME_CONFIG = {
    "bloody-bastards": {
        "slug": "bloody-bastards",
        "name": "Bloody Bastards",
    },
    "DATA-WING": {
        "slug": "data-wing",
        "name": "DATA WING",
    },
    "wplace.live": {
        "slug": "wplace-live",
        "name": "Wplace.live",
    },
}
GAME_ORDER = {"bloody-bastards": 0, "DATA-WING": 1, "wplace.live": 2}

EVIDENCE_LABELS = {
    "Resmî Kaynak": "official_source",
    "Oyun İçi Gözlem": "in_game_observation",
    "Kaynak": "reference_source",
    "Öneri": "recommendation",
}
LABEL_PATTERN = re.compile(
    r"\[(Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\]"
)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
SECTION_PATTERN = re.compile(r"(?m)^##\s+(.+?)\s*$")

QUESTION_OVERRIDES = {
    ("bloody-bastards", "İlerleme ve seviye sistemi"):
        "Oyunda ilerleme ve seviye sistemi nasıl çalışıyor?",
    ("bloody-bastards", "Türkçe dil desteği"):
        "Oyunda Türkçe dil desteği var mı?",
    ("bloody-bastards", "Çok oyunculu eşleştirme ve sürüm koşulları"):
        "Çok oyunculu eşleştirme ve sürüm koşulları nasıl işliyor?",
    ("wplace.live", "Türkçe arayüz desteği"):
        "Oyunda Türkçe arayüz desteği var mı?",
}

REQUIRED_FIELDS = {
    "id", "language", "game", "game_slug", "record_type", "question",
    "answer", "answer_markdown", "evidence_types", "sources",
    "content_url", "license", "schema_version",
}


def slugify(value: str) -> str:
    value = value.lower().replace("ı", "i")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def plain_text(markdown: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", markdown)
    text = re.sub(
        r"\[(?:Resmî Kaynak|Oyun İçi Gözlem|Kaynak|Öneri)\]"
        r"(?:\([^)]*\))?",
        "",
        text,
    )
    text = LINK_PATTERN.sub(r"\1", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s+", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = re.sub(r"(?m)^\s*\d+[.)]\s+", "", text)
    text = re.sub(r"(\*\*|__)(.*?)\1", r"\2", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", text)
    text = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)", r"\1", text)
    text = re.sub(chr(96) + r"([^" + chr(96) + r"]+)" + chr(96), r"\1", text)
    return " ".join(text.split()).strip()


def question_for(game_dir: str, heading: str) -> str | None:
    if "?" in heading or "？" in heading:
        return heading
    return QUESTION_OVERRIDES.get((game_dir, heading))


def extract_records(path: Path) -> list[dict[str, Any]]:
    game_dir = path.parent.name
    game = GAME_CONFIG.get(game_dir)
    if game is None:
        game = {
            "slug": slugify(game_dir),
            "name": game_dir.replace("-", " ").replace(".", " ").title(),
        }

    markdown = path.read_text(encoding="utf-8")
    matches = list(SECTION_PATTERN.finditer(markdown))
    records: list[dict[str, Any]] = []
    content_path = path.relative_to(ROOT).with_suffix("").as_posix()
    content_url = f"{SITE_BASE}{content_path}/"

    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        answer_markdown = markdown[start:end].strip()
        question = question_for(game_dir, heading)

        # Empty and non-question sections are deliberately excluded from this FAQ dataset.
        if not question or not plain_text(answer_markdown):
            continue

        evidence_types: list[str] = []
        for label_match in LABEL_PATTERN.finditer(answer_markdown):
            value = EVIDENCE_LABELS[label_match.group(1)]
            if value not in evidence_types:
                evidence_types.append(value)

        sources: list[dict[str, str]] = []
        seen_sources: set[tuple[str, str]] = set()
        for link_match in LINK_PATTERN.finditer(answer_markdown):
            label, url = link_match.groups()
            item = (label, url)
            if item not in seen_sources:
                sources.append({"label": label, "url": url})
                seen_sources.add(item)

        record = {
            "id": f"{game['slug']}-{slugify(question)}",
            "language": "tr",
            "game": game["name"],
            "game_slug": game["slug"],
            "record_type": "faq",
            "question": question,
            "answer": plain_text(answer_markdown),
            "answer_markdown": answer_markdown,
            "evidence_types": evidence_types,
            "sources": sources,
            "content_url": content_url,
            "license": "CC-BY-4.0",
            "schema_version": SCHEMA_VERSION,
        }
        missing = REQUIRED_FIELDS - record.keys()
        if missing:
            raise ValueError(f"{path}: required fields missing: {sorted(missing)}")
        records.append(record)

    return records


def jsonl(records: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in records
    )


def build_outputs() -> dict[str, str]:
    faq_paths = sorted(
        ROOT.glob("oyunlar/*/sik-sorulan-sorular.md"),
        key=lambda path: (GAME_ORDER.get(path.parent.name, 99), path.as_posix()),
    )
    if not faq_paths:
        raise ValueError("No FAQ Markdown files were found.")

    by_game: dict[str, list[dict[str, Any]]] = {}
    source_files: list[str] = []
    all_records: list[dict[str, Any]] = []

    for path in faq_paths:
        game_dir = path.parent.name
        game = GAME_CONFIG.get(game_dir, {
            "slug": slugify(game_dir),
            "name": game_dir.replace("-", " ").replace(".", " ").title(),
        })
        records = extract_records(path)
        source_files.append(path.relative_to(ROOT).as_posix())
        if records:
            by_game.setdefault(game["slug"], []).extend(records)
            all_records.extend(records)

    ids = [record["id"] for record in all_records]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate record IDs were generated.")

    output: dict[str, str] = {}
    all_filename = "oyun-rehberi-sss-v1.jsonl"
    output[all_filename] = jsonl(all_records)

    game_names = {
        config["slug"]: config["name"] for config in GAME_CONFIG.values()
    }
    game_filenames: dict[str, str] = {}
    for game_slug, records in by_game.items():
        filename = f"{game_slug}-sss-v1.jsonl"
        game_filenames[game_slug] = filename
        output[filename] = jsonl(records)

    file_entries = [{
        "path": all_filename,
        "scope": "all_games",
        "format": "jsonl",
        "records": len(all_records),
    }]
    for game_slug, filename in game_filenames.items():
        file_entries.append({
            "path": filename,
            "scope": "game",
            "game": game_names.get(game_slug, game_slug),
            "game_slug": game_slug,
            "format": "jsonl",
            "records": len(by_game[game_slug]),
        })

    manifest = {
        "name": "Oyun-Rehberi SSS Veri Kümesi",
        "dataset_version": DATASET_VERSION,
        "schema_version": SCHEMA_VERSION,
        "language": "tr",
        "record_type": "faq",
        "format": "JSON Lines (UTF-8), one JSON object per line",
        "license": "CC-BY-4.0",
        "source_repository": "https://github.com/OyuncuSempanze/Oyun-Rehberi",
        "website": SITE_BASE,
        "description": (
            "Mevcut oyun SSS sayfalarından üretilen Türkçe soru-cevap kayıtları. "
            "Kaynak bağlantıları ve bilgi türü etiketleri kayıtlarda korunur."
        ),
        "record_count": len(all_records),
        "source_files": source_files,
        "files": file_entries,
        "schema_url": f"{SITE_BASE}veri-kumeleri/schema-v1.json",
        "rights_notice": (
            "CC BY 4.0 lisansı yalnızca arşivin lisanslama yetkisine sahip olduğu "
            "özgün metin ve düzenleme unsurlarına uygulanır. Kaynak bağlantıları ve "
            "üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir."
        ),
        "limitations": [
            "This is an FAQ export, not a claim that the dataset is ready for every model-training task.",
            "Empty headings and sections without a curated question are omitted.",
            "Source URLs identify references, but do not independently prove that a claim is correct.",
        ],
    }
    output["manifest.json"] = json.dumps(
        manifest, ensure_ascii=False, indent=2
    ) + "\n"
    return output


def check_jsonl_outputs(outputs: dict[str, str]) -> None:
    for filename, content in outputs.items():
        if not filename.endswith(".jsonl"):
            continue
        seen: set[str] = set()
        for line_number, line in enumerate(content.splitlines(), start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{filename}:{line_number}: invalid JSON: {error}"
                ) from error
            missing = REQUIRED_FIELDS - record.keys()
            if missing:
                raise ValueError(
                    f"{filename}:{line_number}: missing fields {sorted(missing)}"
                )
            if not record["question"].strip() or not record["answer"].strip():
                raise ValueError(
                    f"{filename}:{line_number}: question and answer must be non-empty"
                )
            if record["id"] in seen:
                raise ValueError(f"{filename}:{line_number}: duplicate ID")
            seen.add(record["id"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify committed exports match the current Markdown FAQ files",
    )
    args = parser.parse_args()

    try:
        outputs = build_outputs()
        check_jsonl_outputs(outputs)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Dataset error: {error}", file=sys.stderr)
        return 1

    if args.check:
        mismatches: list[str] = []
        for filename, expected in outputs.items():
            path = OUTPUT_DIR / filename
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                mismatches.append(filename)

        expected_jsonl = {
            filename for filename in outputs if filename.endswith(".jsonl")
        }
        if OUTPUT_DIR.exists():
            for path in OUTPUT_DIR.glob("*-sss-v1.jsonl"):
                if path.name not in expected_jsonl:
                    mismatches.append(path.name + " (stale file)")

        if mismatches:
            print(
                "Generated data files are out of date. Run "
                "'python scripts/build_dataset.py' and commit the outputs:",
                file=sys.stderr,
            )
            for filename in sorted(set(mismatches)):
                print(f"- {filename}", file=sys.stderr)
            return 1

        count = len(outputs["oyun-rehberi-sss-v1.jsonl"].splitlines())
        print(f"Dataset check passed: {count} records.")
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in outputs.items():
        path = OUTPUT_DIR / filename
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Generated {len(outputs)} files in {OUTPUT_DIR.relative_to(ROOT)}.")
    print(f"Total records: {len(outputs['oyun-rehberi-sss-v1.jsonl'].splitlines())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
