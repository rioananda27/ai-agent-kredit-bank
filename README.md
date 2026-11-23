[README.md](https://github.com/user-attachments/files/35267703/README.md)
# AI Agent Magang: Administrasi Kredit Bank

Repository ini berisi rancangan dan prototipe **Agent Pemeriksa Kelengkapan Dokumen Pengajuan Kredit** untuk studi kasus magang di bagian kredit bank.

## 1. Latar belakang

Petugas administrasi kredit menerima dan memeriksa berkas pengajuan. Sebagian pemeriksaan bersifat berulang, misalnya mencocokkan daftar dokumen wajib, memeriksa apakah dokumen sudah diterima, mengecek tanggal dokumen yang memiliki batas kebaruan, lalu membuat daftar kekurangan.

Project ini mengusulkan Agent untuk mengotomatisasi pemeriksaan administratif tersebut berdasarkan aturan produk kredit yang telah ditetapkan bank.

> **Batas tugas Agent:** Agent hanya memeriksa kelengkapan administratif dan kebaruan dokumen. Agent **tidak** menilai kelayakan kredit, menghitung kemampuan membayar sebagai keputusan akhir, memberi rekomendasi persetujuan, atau menyetujui/menolak pengajuan. Keputusan kredit tetap berada pada pejabat/pegawai berwenang sesuai kebijakan bank.

## 2. Ruang lingkup otomatisasi

Agent dapat secara otomatis:

1. Membaca daftar pengajuan dari berkas JSON.
2. Mencocokkan dokumen yang diterima dengan daftar dokumen wajib pada konfigurasi produk.
3. Menandai dokumen yang belum diterima.
4. Memeriksa kebaruan dokumen yang memiliki batas usia dokumen, misalnya bukti penghasilan atau rekening koran pada aturan simulasi.
5. Mengidentifikasi dokumen yang belum dapat diperiksa karena status atau tanggalnya tidak jelas.
6. Menghasilkan status administratif dan daftar tindak lanjut.
7. Menyimpan hasil pemeriksaan dalam JSON.

Semua aturan pada contoh ini adalah **data simulasi untuk pembelajaran**, bukan ketentuan resmi bank. Persyaratan nyata berbeda menurut bank, produk, jenis pemohon, dan kebijakan yang berlaku.

## 3. Struktur repository

```text
ai-agent-kredit-bank/
├── README.md
├── .gitignore
├── docs/
│   ├── 01-identifikasi-jobdesk.md
│   ├── 02-aktivitas-repetitif.md
│   ├── 03-rancangan-agent.md
│   ├── 04-keamanan-dan-batasan.md
│   └── 05-skenario-pengujian.md
├── agents/
│   └── pemeriksa-kelengkapan-dokumen.md
├── workflows/
│   └── credit-document-checker.mmd
├── configs/
│   └── required_documents.json
├── data/
│   └── sample_applications.json
├── src/
│   └── credit_checker.py
├── tests/
│   └── test_credit_checker.py
└── examples/
    └── .gitkeep
```

## 4. Cara menjalankan prototipe

### Persyaratan

- Python 3.9 atau lebih baru.
- Tidak memerlukan library tambahan; prototipe menggunakan standard library Python.

### Jalankan pemeriksaan contoh

Dari direktori utama repository:

```bash
python src/credit_checker.py \
  --input data/sample_applications.json \
  --config configs/required_documents.json \
  --as-of 2026-11-23 \
  --output examples/sample_output.json
```

Di Windows Command Prompt, jalankan dalam satu baris:

```bat
python src/credit_checker.py --input data/sample_applications.json --config configs/required_documents.json --as-of 2026-11-23 --output examples/sample_output.json
```

Hasil pemeriksaan akan disimpan di `examples/sample_output.json`.

### Jalankan pengujian

```bash
python -m unittest discover -s tests -v
```

## 5. Arti status hasil

| Status | Arti |
|---|---|
| `LENGKAP` | Semua dokumen wajib pada konfigurasi simulasi diterima dan lolos pemeriksaan tanggal. |
| `BELUM_LENGKAP` | Ada dokumen wajib yang belum diterima atau sudah melewati batas kebaruan yang ditentukan. |
| `PERLU_VERIFIKASI` | Ada data yang tidak terbaca, tidak dikenal, atau tanggal yang perlu dikonfirmasi. |

Status tersebut adalah **status administrasi berkas**, bukan keputusan kredit.

## 6. Hal yang belum dilakukan prototipe

Prototipe saat ini membaca metadata dokumen yang sudah disusun dalam JSON. Prototipe ini belum:

- membaca foto atau PDF dokumen menggunakan OCR;
- terhubung ke core banking, loan origination system, email, atau penyimpanan bank;
- memverifikasi keaslian dokumen ke instansi penerbit;
- melakukan analisis risiko atau credit scoring;
- mengirim permintaan dokumen kepada nasabah.

Pada penerapan nyata, fitur tersebut memerlukan integrasi resmi, kontrol akses, audit trail, pengamanan data, pengujian, dan persetujuan bank. Gunakan hanya data dummy pada repository GitHub publik.
4. Tambahkan audit log dan hak akses.
5. Lakukan pengujian dengan kasus normal, dokumen hilang, dokumen kedaluwarsa/tidak mutakhir, dan data tidak terbaca.

## 9. Etika dan penggunaan data

Jangan unggah KTP, NPWP, slip gaji, rekening koran, data rekening, atau informasi nasabah sungguhan ke GitHub. Gunakan data simulasi yang tidak merujuk pada individu nyata. Ikuti kebijakan keamanan informasi dan perlindungan data bank tempat magang.
