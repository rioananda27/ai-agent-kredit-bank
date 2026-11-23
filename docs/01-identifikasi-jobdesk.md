# 01. Identifikasi Jobdesk Bagian Kredit Bank

## Tujuan

Mengidentifikasi tugas administrasi pada bagian kredit yang memiliki langkah berulang dan dapat diotomatisasi menggunakan Agent.

## Contoh jobdesk bagian kredit

| Jobdesk | Aktivitas | Potensi otomatisasi |
|---|---|---|
| Penerimaan berkas | Mencatat pengajuan dan dokumen yang diterima | Tinggi, jika data masuk secara digital dan formatnya terstruktur |
| Pemeriksaan kelengkapan | Mencocokkan dokumen dengan checklist produk | Tinggi, karena berbasis aturan |
| Pemeriksaan kebaruan dokumen | Memeriksa tanggal dokumen yang memiliki batas usia | Tinggi, jika tanggal dapat dibaca dengan benar dan aturan tersedia |
| Pengelompokan berkas | Mengelompokkan dokumen per nomor pengajuan dan jenis dokumen | Tinggi, jika penamaan/metadata konsisten |
| Pembuatan daftar kekurangan | Membuat daftar dokumen yang belum diterima | Tinggi |
| Pemberitahuan kekurangan | Menyiapkan atau mengirim pemberitahuan standar | Dapat otomatis jika kanal, template, dan izin pengiriman sudah disetujui |
| Analisis kelayakan kredit | Menilai risiko dan kemampuan membayar | Tidak menjadi ruang lingkup Agent ini; memerlukan proses dan kewenangan bank |
| Keputusan kredit | Menyetujui atau menolak permohonan | Tidak dilakukan oleh Agent ini |

## Kesimpulan

Aktivitas yang paling tepat dipilih adalah pemeriksaan kelengkapan administratif dokumen pengajuan kredit. Alurnya berulang, kriterianya dapat dituliskan dalam aturan, dan hasilnya dapat diperiksa kembali. Agent tidak menggantikan analisis maupun keputusan kredit.
