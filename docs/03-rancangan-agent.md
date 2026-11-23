# 03. Rancangan AI Agent

## Nama Agent

**Credit Document Completeness Agent** (Agent Pemeriksa Kelengkapan Dokumen Kredit).

## Tujuan

Mengotomatisasi pemeriksaan administratif awal atas dokumen pengajuan kredit berdasarkan checklist dan aturan kebaruan dokumen yang telah dikonfigurasi.

## Input

- ID pengajuan (kode simulasi).
- Kode produk kredit.
- Daftar dokumen.
- Jenis dokumen.
- Status penerimaan dokumen.
- Tanggal dokumen jika aturan produk mengharuskannya.

## Proses

1. Membaca pengajuan.
2. Memastikan kode produk tersedia dalam konfigurasi.
3. Memuat daftar dokumen wajib.
4. Mencari dokumen berdasarkan tipe.
5. Memeriksa status penerimaan.
6. Memeriksa kebaruan dokumen jika ada batas usia.
7. Menandai data yang tidak valid atau ambigu untuk verifikasi.
8. Menghasilkan hasil pemeriksaan dan daftar tindak lanjut.

## Output

- ID pengajuan.
- Status administrasi.
- Daftar dokumen wajib yang lengkap.
- Daftar dokumen yang belum diterima.
- Daftar dokumen yang tidak mutakhir.
- Daftar item yang perlu verifikasi.
- Catatan bahwa hasil bukan keputusan kredit.

## Aturan keputusan administratif

| Kondisi | Hasil item |
|---|---|
| Dokumen wajib tidak tercantum atau berstatus `missing` | `MISSING` |
| Dokumen berstatus `unreadable` atau status tidak dikenal | `NEEDS_REVIEW` |
| Dokumen wajib memiliki batas usia tetapi tanggalnya kosong/tidak valid | `NEEDS_REVIEW` |
| Tanggal dokumen lebih lama dari batas usia yang ditentukan | `OUTDATED` |
| Dokumen diterima dan lolos aturan tanggal | `ACCEPTED` |

Status akhir:

- Ada `MISSING` atau `OUTDATED` → `BELUM_LENGKAP`.
- Tidak ada kekurangan, tetapi ada `NEEDS_REVIEW` → `PERLU_VERIFIKASI`.
- Semua dokumen wajib `ACCEPTED` → `LENGKAP`.

## Batas kewenangan

Agent tidak melakukan credit scoring, analisis kemampuan membayar, penilaian karakter nasabah, deteksi kecurangan sebagai kesimpulan final, atau keputusan persetujuan/penolakan kredit. Agent hanya memberi hasil pemeriksaan administratif sesuai aturan yang diberikan.
