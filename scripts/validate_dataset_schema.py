#!/usr/bin/env python3
"""Validate every exported JSONL record against the published JSON Schema."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "veri-kumeleri"
SCHEMA_PATH = DATASET_DIR / "schema-v1.json"


def main() -> int:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, Exception) as error:
        print(f"Schema error in {SCHEMA_PATH.relative_to(ROOT)}: {error}", file=sys.stderr)
        return 1

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    files = sorted(DATASET_DIR.glob("*.jsonl"))
    if not files:
        print("No JSONL exports found.", file=sys.stderr)
        return 1

    record_count = 0
    errors_found = 0
    for path in files:
        with path.open(encoding="utf-8") as stream:
            for line_number, raw_line in enumerate(stream, start=1):
                if not raw_line.strip():
                    print(f"{path.relative_to(ROOT)}:{line_number}: blank lines are not valid JSONL records.", file=sys.stderr)
                    errors_found += 1
                    continue
                try:
                    record = json.loads(raw_line)
                except json.JSONDecodeError as error:
                    print(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {error.msg}.", file=sys.stderr)
                    errors_found += 1
                    continue

                record_count += 1
                validation_errors = sorted(
                    validator.iter_errors(record),
                    key=lambda error: (list(map(str, error.absolute_path)), error.message),
                )
                for error in validation_errors:
                    location = "/".join(str(part) for part in error.absolute_path) or "<record>"
                    print(
                        f"{path.relative_to(ROOT)}:{line_number}:{location}: {error.message}",
                        file=sys.stderr,
                    )
                    errors_found += 1

    if errors_found:
        print(f"Schema validation failed: {errors_found} error(s) in {record_count} record(s).", file=sys.stderr)
        return 1

    print(f"JSON Schema check passed: {len(files)} files, {record_count} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
