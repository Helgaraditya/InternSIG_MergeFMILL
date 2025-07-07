# 🚀 FMILL Data Merger - PT Semen Indonesia
Skrip Python ini dibuat untuk menggabungkan otomatis data laporan harian Finish Mill (FMILL#1 hingga FMILL#9) dari berbagai file Excel bulanan. File yang digabungkan berada di dalam subfolder berdasarkan nama bulan (JAN, FEB, MAR, dst), dan setiap file memiliki 9 sheet (FMILL#1 sampai FMILL#9) dengan struktur kolom yang berbeda.
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


