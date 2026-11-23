# 02. Aktivitas Repetitif yang Dapat Diotomatisasi

## Aktivitas terpilih

**Pemeriksaan kelengkapan dokumen pengajuan kredit berdasarkan checklist produk.**

## Pekerjaan manual yang berulang

1. Membuka data atau map pengajuan.
2. Melihat jenis produk kredit yang diajukan.
3. Membuka checklist dokumen wajib untuk produk tersebut.
4. Mencocokkan satu per satu dokumen yang telah diterima.
5. Memeriksa tanggal pada dokumen yang memiliki ketentuan kebaruan.
6. Mencatat dokumen yang belum ada atau perlu diperiksa ulang.
7. Membuat ringkasan status kelengkapan berkas.

## Bagian yang dikerjakan Agent

| Langkah | Tindakan otomatis | Output |
|---|---|---|
| 1 | Membaca daftar pengajuan digital | Data pengajuan terbaca |
| 2 | Memuat aturan dokumen wajib berdasarkan kode produk | Checklist yang sesuai |
| 3 | Mencocokkan tipe dan status setiap dokumen | Daftar dokumen diterima/hilang |
| 4 | Memeriksa tanggal dokumen yang dibatasi usia | Dokumen mutakhir/tidak mutakhir/perlu verifikasi |
| 5 | Menetapkan status administratif berdasarkan aturan | LENGKAP, BELUM_LENGKAP, atau PERLU_VERIFIKASI |
| 6 | Membuat ringkasan hasil | Laporan JSON |

## Syarat agar berjalan otomatis

- Data pengajuan tersedia secara digital.
- Jenis dokumen memiliki nama/identitas yang konsisten.
- Checklist resmi untuk setiap produk telah dikonfigurasi oleh pihak bank.
- Aturan batas kebaruan dokumen ditetapkan oleh pihak berwenang.
- Sistem mendapat akses hanya ke data yang memang diizinkan.

## Catatan

Dalam prototipe ini, metadata dokumen dimasukkan ke JSON. Jika nantinya Agent membaca PDF atau foto secara langsung, diperlukan OCR dan langkah verifikasi hasil ekstraksi. Dokumen yang tidak terbaca tidak boleh diasumsikan valid.
