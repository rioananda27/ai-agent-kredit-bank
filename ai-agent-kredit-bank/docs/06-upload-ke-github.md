# 06. Cara Mengunggah Project ke GitHub

## Cara paling mudah: GitHub Desktop

1. Ekstrak ZIP project ke komputer.
2. Instal dan buka GitHub Desktop: https://desktop.github.com/.
3. Login ke akun GitHub.
4. Pilih **File → Add Local Repository** dan pilih folder `ai-agent-kredit-bank`.
5. Jika folder belum memiliki Git repository, pilih opsi untuk membuat repository di folder tersebut.
6. Isi ringkasan commit, misalnya `Initial commit - credit document checker`.
7. Klik **Commit to main**.
8. Klik **Publish repository**, tentukan nama repository dan visibilitasnya, lalu publish.

GitHub Desktop mengunggah seluruh direktori kerja beserta subfolder. Tidak perlu mengunggah folder satu per satu.

## Alternatif: terminal Git

Buat repository kosong di GitHub terlebih dahulu. Jangan membuat README tambahan di halaman GitHub jika README sudah ada di folder lokal. Buka terminal pada folder `ai-agent-kredit-bank`, lalu jalankan:

```bash
git init
git add .
git commit -m "Initial commit - credit document checker"
git branch -M main
git remote add origin https://github.com/USERNAME/ai-agent-kredit-bank.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub sendiri.

## Pemeriksaan setelah upload

Pastikan halaman repository menampilkan folder `agents`, `configs`, `data`, `docs`, `examples`, `src`, `tests`, dan `workflows`, serta file `README.md` dan `.gitignore`.

**Penting:** Jangan mengunggah data nasabah sungguhan. Isi folder `data` pada project ini adalah data simulasi.
