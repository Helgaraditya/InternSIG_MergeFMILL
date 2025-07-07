# 📊 Merge Data Finish Mill - PT Semen Indonesia

Skrip Python ini digunakan untuk **menggabungkan otomatis data laporan harian Finish Mill (FMILL)** dari file Excel bulanan. Data terdapat di dalam sheet bernama `FMILL#1` hingga `FMILL#9`, masing-masing mewakili lini produksi yang berbeda. Setiap sheet memiliki struktur kolom berbeda, sehingga dilakukan penyesuaian saat proses merge.

---

## 📁 Struktur Folder
📦admpbp - PRODUKSI
┣ 📂JAN
┃ ┗ 📄Tuban Fmill jan_25r.xlsx
┣ 📂FEB
┃ ┗ 📄Tuban Fmill feb_25r.xlsx
┣ 📂...
┗ 📂DES
┗ 📄Tuban Fmill des_25r.xlsx


---

## 📌 Fitur Utama

- ✅ Membaca sheet FMILL#1 hingga FMILL#9 per bulan
- 🔁 Struktur kolom fleksibel:
  - **FMILL#1–4** memiliki 11 kolom
  - **FMILL#5–9** memiliki 15 kolom
- 🧩 Menstandarisasi kolom agar seluruh sheet bisa digabung
- 0️⃣ Mengisi kolom yang tidak tersedia dengan nilai `0`
- 📅 Menambahkan kolom `tanggal`, `FMILL`, `Bulan`, dan `SourceFilePath`
- ➕ Hanya menambahkan data baru ke file hasil gabungan
- 📝 Menyimpan log proses otomatis ke dalam file `log_merge_fmill.txt`

---


