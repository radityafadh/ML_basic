import numpy as np
import pandas as pd

# === Series ===

# Membuat Series (1 kolom) dari 0 sampai 999, index default (0-999)
dataset1 = pd.Series(np.arange(1000))

print("ini adalah head dari dataset 1 = \n", dataset1.head())  # Tampilkan 5 data pertama
print("ini adalah info dari dataset 1 = \n", dataset1.info())  # Informasi struktur Series
print("ini adalah describe dari dataset 1 = \n", dataset1.describe())  # Statistik deskriptif

# Membuat Series dengan index dari 1000 sampai 1999
dataset2 = pd.Series(np.arange(1000), index=np.arange(1000, 2000))

print("ini adalah head dari dataset 2 = \n", dataset2.head())  # Menampilkan 5 data pertama
print("ini adalah value dari index misal 1002 = \n", dataset2[1002])  # Mengakses via label index
print("ini adalah value urutan ke 989 = \n", dataset2.iloc[989])  # Mengakses via posisi index
print("meminta index dari misal 1023-1057 = \n", dataset2.index[1023:1057])  # Slice index

# Conditional selection: mencari nilai > 500
dataset3 = pd.Series(np.arange(1000), index=np.arange(1000, 2000))

print("berikan keterangan boolean mana yang di atas dari 500 = \n", dataset3 > 500)  # Boolean mask
print("berikan keterangan number mana yang di atas 500 = \n", dataset3[dataset3 > 500])  # Nilai sebenarnya

# === DataFrame ===

# Membuat DataFrame sederhana dengan 3 kolom dan 3 baris
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})
print(df)

# Mengubah index secara manual
print("mengubah index = \n")
df.index = ["data satu", "data dua", "data tiga"]
print(df)

# Atau menggunakan for-loop untuk menyetel index
df.index = ["data " + str(i + 1) for i in range(len(df))]
print("setelah menggunakan loop = \n", df)

# Statistik deskriptif
print("describe = \n", df.describe())  # Mean, std, min, max, dll.
print("info = \n", df.info())          # Struktur DataFrame
print("head = \n", df.head())          # 5 baris pertama
print("tail = \n", df.tail())          # 5 baris terakhir

# Mengakses data berdasarkan index label
print("mengambil index data dua = \n", df.loc["data 2"])  # Mengakses baris "data 2"
print("mengambil index data dua dan C, dengan variabel A dan B = \n", df.loc["data 2", ["A", "B"]])

# === Conditional Selection ===

# Boolean mask: mana nilai yang lebih dari 2
print("berikan keterangan boolean mana yang di atas dari 2 = \n", df > 2)
print("berikan keterangan number mana yang di atas 2 = \n", df[df > 2])

# === Modifikasi DataFrame ===

# Menghapus baris berdasarkan label index
df.drop("data 2", inplace=True)
print("menghapus data dua = \n", df)

# Menambahkan 10 ke kolom B (hasil tanpa mengubah DataFrame asli)
print("menambah angka di kolom B = \n", df["B"] + 10)

# Mengganti nama kolom dan index (rename)
print("mengganti value di kolom B = \n", df.rename(columns={"B": "D"}, index={"data 1": "data setunggal"}))

# Menambahkan kolom baru 'E' sebagai hasil penjumlahan kolom A dan C
df["E"] = df["A"] + df["C"]
print("membuat kolom baru = \n", df)
