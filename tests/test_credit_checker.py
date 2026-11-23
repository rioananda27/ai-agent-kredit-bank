import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from src.credit_checker import check_application, validate_config, CreditCheckerError


CONFIG = {
    "products": {
        "DEMO": {
            "display_name": "Produk Demo",
            "required_documents": [
                {"type": "form", "label": "Formulir", "max_age_days": None},
                {"type": "income", "label": "Bukti penghasilan", "max_age_days": 90},
            ],
        }
    }
}
AS_OF = date(2026, 11, 23)


def app(documents):
    return {
        "application_id": "TEST-001",
        "product_code": "DEMO",
        "documents": documents,
    }


class CreditCheckerTests(unittest.TestCase):
    def setUp(self):
        self.config = validate_config(CONFIG)

    def test_complete_application(self):
        result = check_application(
            app([
                {"document_type": "form", "status": "received"},
                {"document_type": "income", "status": "received", "document_date": "2026-10-01"},
            ]),
            self.config,
            AS_OF,
        )
        self.assertEqual(result["administrative_status"], "LENGKAP")

    def test_missing_document(self):
        result = check_application(
            app([{"document_type": "form", "status": "received"}]),
            self.config,
            AS_OF,
        )
        self.assertEqual(result["administrative_status"], "BELUM_LENGKAP")
        self.assertIn("income", result["missing_documents"])

    def test_outdated_document(self):
        result = check_application(
            app([
                {"document_type": "form", "status": "received"},
                {"document_type": "income", "status": "received", "document_date": "2026-06-01"},
            ]),
            self.config,
            AS_OF,
        )
        self.assertEqual(result["administrative_status"], "BELUM_LENGKAP")
        self.assertIn("income", result["outdated_documents"])

    def test_unreadable_document_needs_review(self):
        result = check_application(
            app([
                {"document_type": "form", "status": "unreadable"},
                {"document_type": "income", "status": "received", "document_date": "2026-10-01"},
            ]),
            self.config,
            AS_OF,
        )
        self.assertEqual(result["administrative_status"], "PERLU_VERIFIKASI")

    def test_unknown_product_is_rejected(self):
        with self.assertRaises(CreditCheckerError):
            check_application(
                {"application_id": "TEST-002", "product_code": "UNKNOWN", "documents": []},
                self.config,
                AS_OF,
            )


if __name__ == "__main__":
    unittest.main()
