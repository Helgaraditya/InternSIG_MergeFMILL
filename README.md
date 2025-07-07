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

## 📐 Struktur Kolom

### FMILL#1 – FMILL#4 (11 Kolom)

| No | Nama Kolom           |
|----|-----------------------|
| 1  | Date                  |
| 2  | Production (TPD)      |
| 3  | Production (TPH)      |
| 4  | KWH/TON               |
| 5  | Running Time          |
| 6  | Running Time (HRC)    |
| 7  | % Run HRC             |
| 8  | Number of Stops       |
| 9  | TYPE SEMEN            |
| 10 | Cause of stop         |
| 11 | In Silo               |

**Catatan**: Untuk menyesuaikan dengan format sheet FMILL#5–9, maka kolom `KWH MILL`, `KWH SEPARATOR`, `KWH Fan`, dan `KWH MAIN` ditambahkan otomatis dengan nilai `0`.

---

### FMILL#5 – FMILL#9 (15 Kolom)

| No | Nama Kolom           |
|----|-----------------------|
| 1  | Date                  |
| 2  | Production (TPD)      |
| 3  | Production (TPH)      |
| 4  | Running Time          |
| 5  | Running Time (HRC)    |
| 6  | % Run HRC             |
| 7  | Number of Stops       |
| 8  | KWH MILL              |
| 9  | KWH SEPARATOR         |
| 10 | KWH Fan               |
| 11 | KWH MAIN              |
| 12 | KWH/TON               |
| 13 | TYPE SEMEN            |
| 14 | Cause of stop         |
| 15 | In Silo               |

---




