# 05. Skenario Pengujian

## Tujuan

Memastikan prototipe memberi status administratif yang sesuai dengan aturan simulasi.

| ID | Skenario | Hasil yang diharapkan |
|---|---|---|
| TC-01 | Semua dokumen wajib diterima dan tanggal masih sesuai | `LENGKAP` |
| TC-02 | Satu dokumen wajib tidak ada | `BELUM_LENGKAP` |
| TC-03 | Dokumen dengan batas usia melewati batas | `BELUM_LENGKAP` |
| TC-04 | Dokumen tidak terbaca | `PERLU_VERIFIKASI` |
| TC-05 | Tanggal dokumen wajib tidak tersedia | `PERLU_VERIFIKASI` |
| TC-06 | Kode produk tidak ada di konfigurasi | Program menampilkan pesan kesalahan yang jelas |

## Cara menjalankan pengujian

```bash
python -m unittest discover -s tests -v
```

## Kriteria keberhasilan

- Status akhir sesuai aturan yang ditetapkan.
- Dokumen yang hilang dan tidak mutakhir ditampilkan.
- Data yang ambigu tidak otomatis dinyatakan lengkap.
- Output menegaskan bahwa hasil bukan keputusan kredit.
