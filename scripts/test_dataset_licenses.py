#!/usr/bin/env python3
"""Regression tests for the project's CC BY 4.0 dataset licensing policy."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_dataset as builder


class DatasetLicenseTests(unittest.TestCase):
    def test_new_content_defaults_to_cc_by_4_0(self) -> None:
        self.assertEqual(builder.DEFAULT_LICENSE, "CC-BY-4.0")
        self.assertEqual(builder.SUPPORTED_LICENSES, {"CC-BY-4.0"})

    def test_noncommercial_license_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            builder.resolve_content_license("Content.", "CC-BY-NC-4.0")

        with self.assertRaises(ValueError):
            builder.resolve_content_license(
                "<!-- dataset-license: CC-BY-NC-4.0 -->\nContent.",
                "CC-BY-4.0",
            )

    def test_duplicate_section_directives_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            builder.resolve_content_license(
                "<!-- dataset-license: CC-BY-4.0 -->\n"
                "<!-- dataset-license: CC-BY-4.0 -->\nContent.",
                "CC-BY-4.0",
            )

    def test_exports_use_cc_by_4_0_and_have_no_extra_permissions(self) -> None:
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

Bu yanıt, veri kümesi lisans testinde kullanılacak kadar uzun ve açıklayıcı bir metin içerir. [Oyun İçi Gözlem]
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

Bu bölüm, açıkça CC BY 4.0 lisansı taşıyan kaynak metindeki uzun bir açıklamayı temsil eder. [Oyun İçi Gözlem]

## Yeni bölüm

Bu bölüm aynı dosyaya sonradan eklenmiştir ve dosyanın varsayılan lisansını devralır. [Oyun İçi Gözlem]
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

Lisans metaverisi bulunmayan yeni kaynak dosyaları varsayılan olarak CC BY 4.0 lisansını kullanmalıdır. [Oyun İçi Gözlem]
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
        guides = {
            record.get("section_title"): record
            for record in records
            if record["record_type"] == "guide_section"
        }
        faq = next(record for record in records if record["record_type"] == "faq")

        self.assertEqual(faq["license"], "CC-BY-4.0")
        self.assertEqual(guides["Eski bölüm"]["license"], "CC-BY-4.0")
        self.assertEqual(guides["Yeni bölüm"]["license"], "CC-BY-4.0")
        self.assertEqual(guides["Yeni içerik"]["license"], "CC-BY-4.0")
        self.assertNotIn("additional_permissions", faq)
        self.assertNotIn("additional_permissions", guides["Yeni içerik"])
        self.assertNotIn("dataset-license", outputs["oyun-rehberi-rehber-bolumleri-v1.jsonl"])

        parent_by_id = {record["id"]: record for record in records}
        self.assertTrue(claims)
        for claim in claims:
            parent = parent_by_id[claim["source_record_id"]]
            self.assertEqual(claim["license"], parent["license"])
            self.assertNotIn("additional_permissions", claim)

        self.assertEqual(manifest["license"], "CC-BY-4.0")
        self.assertEqual(
            {item["identifier"] for item in manifest["licenses"]},
            {"CC-BY-4.0"},
        )
        self.assertEqual(manifest["record_count"], len(records))
        self.assertEqual(manifest["claim_unit_count"], len(claims))
        self.assertNotIn("additional_permissions", manifest)
        self.assertEqual(
            sum(item["records"] for item in manifest["files"] if item["scope"] == "all_records"),
            len(records),
        )
        self.assertEqual(
            sum(item["records"] for item in manifest["files"] if item["scope"] == "claim_units"),
            len(claims),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
