#!/usr/bin/env python3
"""Administrative document checklist prototype for a simulated bank-credit workflow.

This is a deterministic rules engine for demonstration. It does not make credit decisions.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

VALID_DOCUMENT_STATUSES = {"received", "missing", "unreadable"}


class CreditCheckerError(Exception):
    """Raised when input/configuration cannot be processed safely."""


def parse_iso_date(value: Any, field_name: str) -> date:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} harus berupa tanggal YYYY-MM-DD.")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{field_name} tidak valid: {value!r}; gunakan YYYY-MM-DD.") from exc


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        raise CreditCheckerError(f"File tidak ditemukan: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CreditCheckerError(f"JSON tidak valid pada {path}: {exc}") from exc


def validate_config(config: Any) -> dict[str, Any]:
    if not isinstance(config, dict) or not isinstance(config.get("products"), dict):
        raise CreditCheckerError("Konfigurasi harus memiliki objek 'products'.")

    for product_code, product in config["products"].items():
        if not isinstance(product, dict):
            raise CreditCheckerError(f"Konfigurasi produk {product_code} harus berupa objek.")
        requirements = product.get("required_documents")
        if not isinstance(requirements, list) or not requirements:
            raise CreditCheckerError(
                f"Produk {product_code} harus memiliki daftar required_documents yang tidak kosong."
            )
        seen: set[str] = set()
        for requirement in requirements:
            if not isinstance(requirement, dict):
                raise CreditCheckerError(f"Aturan dokumen pada produk {product_code} tidak valid.")
            doc_type = requirement.get("type")
            if not isinstance(doc_type, str) or not doc_type.strip():
                raise CreditCheckerError("Setiap aturan dokumen harus memiliki 'type'.")
            if doc_type in seen:
                raise CreditCheckerError(f"Tipe dokumen duplikat di konfigurasi: {doc_type}.")
            seen.add(doc_type)
            max_age = requirement.get("max_age_days")
            if max_age is not None and (not isinstance(max_age, int) or max_age < 0):
                raise CreditCheckerError(f"max_age_days untuk {doc_type} harus bilangan bulat >= 0 atau null.")
    return config


def evaluate_document(
    requirement: dict[str, Any],
    submitted_documents: list[dict[str, Any]],
    as_of: date,
) -> dict[str, Any]:
    doc_type = requirement["type"]
    label = requirement.get("label", doc_type)
    matching = [doc for doc in submitted_documents if doc.get("document_type") == doc_type]

    if not matching:
        return {
            "document_type": doc_type,
            "label": label,
            "status": "MISSING",
            "detail": "Dokumen wajib belum tercatat diterima.",
        }

    # More than one record for the same required type is ambiguous; do not silently choose one.
    if len(matching) > 1:
        return {
            "document_type": doc_type,
            "label": label,
            "status": "NEEDS_REVIEW",
            "detail": f"Ditemukan {len(matching)} catatan untuk tipe dokumen yang sama.",
        }

    document = matching[0]
    status = document.get("status")
    if status not in VALID_DOCUMENT_STATUSES:
        return {
            "document_type": doc_type,
            "label": label,
            "status": "NEEDS_REVIEW",
            "detail": "Status dokumen tidak dikenal atau tidak tersedia.",
        }

    if status == "missing":
        return {
            "document_type": doc_type,
            "label": label,
            "status": "MISSING",
            "detail": "Catatan menunjukkan dokumen belum diterima.",
        }

    if status == "unreadable":
        return {
            "document_type": doc_type,
            "label": label,
            "status": "NEEDS_REVIEW",
            "detail": "Dokumen ditandai tidak terbaca dan perlu pemeriksaan petugas.",
        }

    max_age_days = requirement.get("max_age_days")
    if max_age_days is not None:
        try:
            document_date = parse_iso_date(document.get("document_date"), "document_date")
        except ValueError as exc:
            return {
                "document_type": doc_type,
                "label": label,
                "status": "NEEDS_REVIEW",
                "detail": str(exc),
            }

        age_days = (as_of - document_date).days
        if age_days < 0:
            return {
                "document_type": doc_type,
                "label": label,
                "status": "NEEDS_REVIEW",
                "detail": "Tanggal dokumen berada di masa depan; perlu verifikasi.",
            }
        if age_days > max_age_days:
            return {
                "document_type": doc_type,
                "label": label,
                "status": "OUTDATED",
                "detail": (
                    f"Usia dokumen {age_days} hari, melewati batas simulasi "
                    f"{max_age_days} hari."
                ),
            }

    return {
        "document_type": doc_type,
        "label": label,
        "status": "ACCEPTED",
        "detail": "Dokumen tercatat diterima dan memenuhi aturan administratif simulasi.",
    }


def check_application(
    application: Any,
    config: dict[str, Any],
    as_of: date,
) -> dict[str, Any]:
    if not isinstance(application, dict):
        raise CreditCheckerError("Setiap pengajuan harus berupa objek JSON.")

    application_id = application.get("application_id")
    product_code = application.get("product_code")
    documents = application.get("documents", [])

    if not isinstance(application_id, str) or not application_id.strip():
        raise CreditCheckerError("Setiap pengajuan harus memiliki application_id.")
    if not isinstance(product_code, str) or product_code not in config["products"]:
        raise CreditCheckerError(
            f"Kode produk untuk pengajuan {application_id} tidak tersedia di konfigurasi: {product_code!r}."
        )
    if not isinstance(documents, list) or any(not isinstance(item, dict) for item in documents):
        raise CreditCheckerError(f"Daftar documents pada {application_id} harus berupa array objek.")

    product = config["products"][product_code]
    results = [
        evaluate_document(requirement, documents, as_of)
        for requirement in product["required_documents"]
    ]

    statuses = {item["status"] for item in results}
    if "MISSING" in statuses or "OUTDATED" in statuses:
        overall_status = "BELUM_LENGKAP"
    elif "NEEDS_REVIEW" in statuses:
        overall_status = "PERLU_VERIFIKASI"
    else:
        overall_status = "LENGKAP"

    return {
        "application_id": application_id,
        "product_code": product_code,
        "product_name": product.get("display_name", product_code),
        "as_of_date": as_of.isoformat(),
        "administrative_status": overall_status,
        "document_results": results,
        "missing_documents": [item["document_type"] for item in results if item["status"] == "MISSING"],
        "outdated_documents": [item["document_type"] for item in results if item["status"] == "OUTDATED"],
        "documents_needing_review": [
            item["document_type"] for item in results if item["status"] == "NEEDS_REVIEW"
        ],
        "disclaimer": "Hasil ini hanya pemeriksaan administratif, bukan keputusan persetujuan atau penolakan kredit.",
    }


def run(input_path: Path, config_path: Path, as_of: date, output_path: Path) -> list[dict[str, Any]]:
    config = validate_config(load_json(config_path))
    applications = load_json(input_path)
    if isinstance(applications, dict):
        applications = [applications]
    if not isinstance(applications, list):
        raise CreditCheckerError("Input harus berupa objek pengajuan atau array pengajuan.")

    results = [check_application(application, config, as_of) for application in applications]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)
        file.write("\n")
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pemeriksa kelengkapan dokumen pengajuan kredit (data simulasi)."
    )
    parser.add_argument("--input", required=True, help="Lokasi file JSON pengajuan.")
    parser.add_argument("--config", required=True, help="Lokasi konfigurasi checklist produk JSON.")
    parser.add_argument("--as-of", help="Tanggal acuan YYYY-MM-DD; default tanggal komputer.")
    parser.add_argument("--output", required=True, help="Lokasi file JSON hasil pemeriksaan.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        as_of = parse_iso_date(args.as_of, "--as-of") if args.as_of else date.today()
        results = run(Path(args.input), Path(args.config), as_of, Path(args.output))
    except (CreditCheckerError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Pemeriksaan selesai: {len(results)} pengajuan.")
    for result in results:
        print(f"- {result['application_id']}: {result['administrative_status']}")
    print(f"Hasil disimpan ke: {args.output}")
    print("Catatan: status administratif ini bukan keputusan kredit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
