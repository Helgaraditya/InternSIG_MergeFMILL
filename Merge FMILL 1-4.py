#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import calendar
import os
import re

# Folder utama
base_folder = r"C:\Users\Helga\semenindonesia.com\admpbp - PRODUKSI"

# Hanya FMILL#1 – FMILL#4
fmill_sheets = [f"FMILL#{i}" for i in range(1, 5)]

# Header 11 kolom untuk FMILL#1 – 4
fmill_header_11 = [
    "Date", "Production (TPD)", "Production (TPH)", "Power (KWH/T)",
    "Running Time", "Running Time (HRC)", "% Run HRC", "Number of Stops",
    "TYPE SEMEN", "Cause of stop", "In Silo"
]

# Folder bulan valid
bulan_folder_valid = {"JAN", "PEB", "MAR", "APR", "MEI", "JUN", "JUL", "AGU", "SEP", "OKT", "NOV", "DES"}

# Pola nama file
valid_pattern_fmill = re.compile(r"^Tuban Fmill [a-z]{3}_25r\.xlsx$", re.IGNORECASE)

# Gabungan data
all_data_fmill = []

for subfolder in os.listdir(base_folder):
    if subfolder.upper() not in bulan_folder_valid:
        continue

    subfolder_path = os.path.join(base_folder, subfolder)
    if not os.path.isdir(subfolder_path):
        continue

    folder_bulan = subfolder.lower()
    expected_filename = f"tuban fmill {folder_bulan}_25r.xlsx"

    for file in os.listdir(subfolder_path):
        if not valid_pattern_fmill.match(file) or file.lower() != expected_filename:
            continue

        full_path = os.path.join(subfolder_path, file)

        try:
            nama_bulan = subfolder.capitalize()
            bulan_num = list(calendar.month_abbr).index(nama_bulan[:3].capitalize())
            tahun = 2025
            jumlah_hari = calendar.monthrange(tahun, bulan_num)[1]
        except:
            continue

        try:
            xl = pd.ExcelFile(full_path)
        except Exception as e:
            print(f" -- Gagal membuka file: {file}, error: {e}")
            continue

        for sheet in fmill_sheets:
            if sheet not in xl.sheet_names:
                print(f" -- Sheet '{sheet}' tidak ditemukan di {file}")
                continue

            try:
                # Kolom G–N dan U–W (melewati kolom tersembunyi O–T)
                df = pd.read_excel(
                    xl,
                    sheet_name=sheet,
                    skiprows=7,
                    usecols=[6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22], 
                    nrows=jumlah_hari,
                    header=None
                )

                df.columns = fmill_header_11
                df.dropna(how="all", inplace=True)
                df["Date"] = pd.to_numeric(df["Date"], errors="coerce")
                df = df[df["Date"].notnull() & df["Date"].between(1, jumlah_hari)]

                df["tanggal"] = pd.to_datetime({
                    "year": tahun,
                    "month": bulan_num,
                    "day": df["Date"].astype(int)
                })

                df["FMILL"] = sheet
                df["Bulan"] = nama_bulan
                df["SourceFilePath"] = full_path

                all_data_fmill.append(df)
                print(f" -- Dibaca: {file} - {sheet}")

            except Exception as e:
                print(f" -- Gagal membaca {file} - {sheet}: {e}")

# Simpan hasil
if all_data_fmill:
    hasil_fmill = pd.concat(all_data_fmill, ignore_index=True)
    hasil_fmill.sort_values(by=["tanggal", "FMILL"], inplace=True)

    output_path = r"D:\MAGANG SIG\TUGAS 2 - MERGE FMILL\FMILL_1_4_FINAL.xlsx"
    hasil_fmill.to_excel(output_path, index=False)
    print(f"\n -- Berhasil disimpan di: {output_path}")
else:
    print("\n -- Tidak ada data yang berhasil dibaca.")


# In[ ]:




