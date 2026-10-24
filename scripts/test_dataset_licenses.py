#!/usr/bin/env python3
"""Regression tests for Markdown-derived dataset license metadata."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_dataset as builder


class DatasetLicenseTests(unittest.TestCase):
    def test_section_directive_overrides_default_and_is_removed(self) -> None:
        markdown = """<!-- dataset-license: CC-BY-NC-4.0 -->
This is a section whose license is explicitly overridden."""
        license_id, cleaned = builder.resolve_content_license(markdown, "CC-BY-4.0")

        self.assertEqual(license_id, "CC-BY-NC-4.0")
        self.assertNotIn("dataset-license", cleaned)
        self.assertIn("explicitly overridden", cleaned)

    def test_unsupported_or_duplicate_directives_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            builder.resolve_content_license(
                "<!-- dataset-license: CC0-1.0 -->\nContent.", "CC-BY-4.0"
            )

        with self.assertRaises(ValueError):
            builder.resolve_content_license(
                "<!-- dataset-license: CC-BY-4.0 -->\n"
                "<!-- dataset-license: CC-BY-NC-4.0 -->\nContent.",
                "CC-BY-4.0",
            )

    def test_exports_preserve_legacy_license_and_track_new_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            game_dir = root / "oyunlar" / "bloody-bastards"
            game_dir.mkdir(parents=True)

            (game_dir / "sik-sorulan-sorular.md").write_text(
                """---
layout: default
title: Eski SSS
license: CC-BY-4.0
---

# Sık Sorulan Sorular

## Eski soru?

Bu eski yanıt veri kümesi lisans testinde kullanılacak kadar uzun ve açıklayıcıdır. [Oyun İçi Gözlem]
""",
                encoding="utf-8",
            )

            (game_dir / "eski-rehber.md").write_text(
                """---
layout: default
title: Eski rehber
license: CC-BY-4.0
---

# Eski rehber

## Eski bölüm

Bu bölüm önceki lisans altında yayımlanan metni temsil eden yeterince uzun bir açıklamadır. [Oyun İçi Gözlem]

## Yeni bölüm

<!-- dataset-license: CC-BY-NC-4.0 -->
Bu bölüm, eski lisanslı bir dosyaya sonradan eklenen ve farklı lisansla yayımlanan yeni içeriği temsil eder. [Oyun İçi Gözlem]
""",
                encoding="utf-8",
            )

            (game_dir / "yeni-rehber.md").write_text(
                """---
layout: default
title: Yeni rehber
---

# Yeni rehber

## Yeni içerik

Lisans metaverisi bulunmayan yeni kaynak dosyaları varsayılan olarak CC BY-NC 4.0 lisansını kullanmalıdır. [Oyun İçi Gözlem]
""",
                encoding="utf-8",
            )

            with patch.object(builder, "ROOT", root), patch.object(
                builder, "SITE_BASE", "https://example.invalid/Oyun-Rehberi/"
            ):
                outputs = builder.build_outputs()

        records = [
            json.loads(line)
            for line in outputs["oyun-rehberi-tam-arsiv-v1.jsonl"].splitlines()
            if line.strip()
        ]
        claims = [
            json.loads(line)
            for line in outputs["oyun-rehberi-iddia-birimleri-v1.jsonl"].splitlines()
            if line.strip()
        ]
        manifest = json.loads(outputs["manifest.json"])
        by_section = {record.get("section_title"): record for record in records if record["record_type"] == "guide_section"}
        faq = next(record for record in records if record["record_type"] == "faq")

        self.assertEqual(faq["license"], "CC-BY-4.0")
        self.assertEqual(by_section["Eski bölüm"]["license"], "CC-BY-4.0")
        self.assertEqual(by_section["Yeni bölüm"]["license"], "CC-BY-NC-4.0")
        self.assertEqual(by_section["Yeni içerik"]["license"], "CC-BY-NC-4.0")
        self.assertEqual(by_section["Yeni bölüm"]["additional_permissions"][0]["identifier"], "OYUN-REHBERI-AI-RETRIEVAL-1.0")
        self.assertEqual(by_section["Yeni içerik"]["additional_permissions"][0]["url"], "https://oyuncusempanze.github.io/Oyun-Rehberi/ai-kullanim/")
        self.assertNotIn("additional_permissions", faq)
        self.assertNotIn("dataset-license", outputs["oyun-rehberi-rehber-bolumleri-v1.jsonl"])

        parent_by_id = {record["id"]: record for record in records}
        self.assertTrue(claims)
        for claim in claims:
            parent = parent_by_id[claim["source_record_id"]]
            self.assertEqual(claim["license"], parent["license"])
            self.assertEqual(claim.get("additional_permissions", []), parent.get("additional_permissions", []))

        self.assertEqual(manifest["license"], "MIXED")
        self.assertEqual(
            {item["identifier"] for item in manifest["licenses"]},
            {"CC-BY-4.0", "CC-BY-NC-4.0"},
        )
        self.assertEqual(manifest["record_count"], len(records))
        self.assertEqual(manifest["claim_unit_count"], len(claims))
        permission = manifest["additional_permissions"][0]
        nc_records = [record for record in records if record["license"] == "CC-BY-NC-4.0"]
        nc_claims = [claim for claim in claims if claim["license"] == "CC-BY-NC-4.0"]
        self.assertEqual(permission["record_count"], len(nc_records))
        self.assertEqual(permission["claim_unit_count"], len(nc_claims))
        self.assertEqual(permission["url"], "https://oyuncusempanze.github.io/Oyun-Rehberi/ai-kullanim/")
        self.assertEqual(sum(item["records"] for item in manifest["files"] if item["scope"] == "all_records"), len(records))
        self.assertEqual(sum(item["records"] for item in manifest["files"] if item["scope"] == "claim_units"), len(claims))


if __name__ == "__main__":
    unittest.main(verbosity=2)
