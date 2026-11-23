# Agent: Pemeriksa Kelengkapan Dokumen Kredit

**Nama teknis:** `credit_document_completeness_agent`

**Peran:** Memeriksa kelengkapan administrasi pengajuan kredit berdasarkan konfigurasi produk yang disetujui.

**Pemicu:** Data pengajuan baru diterima atau petugas meminta pemeriksaan ulang.

**Sumber data:** Metadata dokumen pengajuan dari sistem/berkas yang diizinkan.

**Tindakan:**
1. Membaca ID pengajuan dan kode produk.
2. Memuat checklist dokumen wajib.
3. Mencocokkan dokumen yang diterima.
4. Memeriksa tanggal dokumen yang memiliki batas kebaruan.
5. Menghasilkan status dan daftar kekurangan.
6. Menyimpan ringkasan hasil.

**Output:** Ringkasan JSON berisi status administrasi dan rincian setiap dokumen.

**Aturan keselamatan:** Jangan membuat keputusan kredit atau menyimpulkan kelayakan nasabah. Jangan mengarang dokumen yang tidak tercantum. Data yang tidak jelas harus ditandai `PERLU_VERIFIKASI`.

**Mode prototipe:** Memproses metadata terstruktur dari JSON. OCR dan integrasi sistem bank belum termasuk.
