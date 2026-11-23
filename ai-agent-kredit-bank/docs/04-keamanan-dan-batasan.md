# 04. Keamanan, Privasi, dan Batasan

## Prinsip penggunaan

- Gunakan data sintetis/dummy untuk demonstrasi dan repository publik.
- Jangan menyimpan identitas, nomor rekening, nomor identitas, alamat, slip gaji, atau rekening koran nasabah nyata di GitHub.
- Batasi akses sistem sesuai kebutuhan tugas.
- Simpan log proses tanpa menyalin data sensitif yang tidak diperlukan.
- Pastikan konfigurasi checklist dan masa berlaku dokumen berasal dari kebijakan resmi yang disetujui bank.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Jenis dokumen salah dikenali | Gunakan tipe dokumen baku; data tidak dikenal diberi status verifikasi |
| Tanggal salah dibaca dari hasil OCR | Jangan otomatis menyatakan valid; tandai untuk verifikasi bila format/tanggal meragukan |
| Checklist tidak sesuai produk | Pisahkan konfigurasi per produk dan gunakan versi aturan yang disetujui |
| Dokumen nasabah terekspos | Gunakan penyimpanan terkontrol dan jangan masukkan data nyata ke repository publik |
| Output dianggap keputusan kredit | Tampilkan penegasan bahwa hasil hanya status administratif |

## Keterbatasan prototipe

Prototipe belum terhubung ke sistem bank, belum melakukan OCR, belum memverifikasi keaslian dokumen, dan belum memproses data nasabah sungguhan. Ini adalah demonstrasi aturan pemeriksaan administratif menggunakan data simulasi.
