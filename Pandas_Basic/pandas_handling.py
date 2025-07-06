import pandas as pd
import numpy as np

# === Membuat DataFrame dari Dictionary ===
data = {
    "Hero": [
        "Arthas", "Thrall", "Jaina", "Illidan", "Sylvanas",
        "Uther", "Gul'dan", "Malfurion", "Kael'thas", "Tyrande",
        "Grom", "Kel'Thuzad", "Cairne", "Anduin", "Vol'jin"
    ],
    "Faction": [
        "Scourge", "Horde", "Alliance", "Illidari", "Forsaken",
        "Alliance", "Legion", "Night Elf", "Blood Elf", "Night Elf",
        "Horde", "Scourge", "Horde", "Alliance", "Horde"
    ],
    "Role": [
        "Death Knight", "Warchief", "Mage", "Demon Hunter", "Ranger",
        "Paladin", "Warlock", "Druid", "Mage", "Priest",
        "Warrior", "Lich", "Chieftain", "Priest", "Shadow Hunter"
    ],
    "Level": [80, 75, 70, 85, 78, 74, 82, 76, 71, 73, 72, 79, 70, 68, 74],
    "HP": [4500, 4000, 3000, 99999, 3500, 3600, 3800, 3900, 3100, 3300, 4100, 3700, 4300, 2900, np.nan],
    "Mana": [2000, np.nan, 3000, 2500, 2700, 1800, np.nan, 2800, 3000, 3200, 1200, 3300, 1000, 3100, 2600],
    "Attack": [320, 280, np.nan, 340, 290, 260, 310, 240, 5, 230, 300, 330, 290, 200, 260],
    "Defense": [200, 210, 150, 190, 160, 220, 170, 180, 150, np.nan, 230, 200, 210, 130, 160],
    "Speed": [6.5, 6.0, 6.8, 7.2, 6.9, 5.5, 5.9, 6.1, 6.4, 6.2, 6.3, 100.0, 5.7, 6.7, 6.0],
    "Special": [
        "Frostmourne", "Chain Lightning", "Blizzard", "Metamorphosis", np.nan,
        "Holy Light", "Shadow Bolt", "Tranquility", "Phoenix", "Phoenix",
        "Berserk", "Frost Nova", "Reincarnation", "Heal", "Heal"
    ]
}

# Membuat DataFrame dengan index kustom
df = pd.DataFrame(data, index=[f"unit_{i+1}" for i in range(15)])

# Tambahkan kolom RoleDetail (Role + RoleType)
df["RoleDetail"] = [
    "Death Knight_Melee", "Warchief_Melee", "Mage_Ranged", "Demon Hunter_Melee", "Ranger_Ranged",
    "Paladin_Melee", "Warlock_Ranged", "Druid_Ranged", "Mage_Ranged", "Priest_Ranged",
    "Warrior_Melee", "Lich_Ranged", "Chieftain_Melee", "Priest_Ranged", "Shadow Hunter_Ranged"
]

# Tambahkan duplikat baris dari unit_2 dan unit_7
duplicate_rows = df.loc[["unit_2", "unit_7"]]
df = pd.concat([df, duplicate_rows])

# Reset index menjadi integer 0-n
df = df.reset_index(drop=True)

# === DETEKSI & TANGANI MISSING VALUE ===
print("Apakah ada missing value? (isnull)\n", df.isnull())
print("Jumlah missing value tiap kolom:\n", df.isnull().sum())

# Dropping missing values
print("Drop semua baris dengan missing value:\n", df.dropna())
print("Drop baris yang punya ≥5 nilai non-null:\n", df.dropna(thresh=5))

# Fill missing values
print("Isi missing value dengan 0:\n", df.fillna(0))
print("Isi missing value dengan MEAN (kolom numerik):\n", df.fillna(df.mean(numeric_only=True)))
print("Isi missing value dengan MEDIAN (kolom numerik):\n", df.fillna(df.median(numeric_only=True)))
print("Isi missing value dengan MODE:\n", df.fillna(df.mode().iloc[0]))

# === DUPLIKAT ===
print("Deteksi duplikat baris (default=keep first):\n", df.duplicated())
print("Deteksi duplikat (keep last):\n", df.duplicated(keep="last"))
print("Deteksi semua duplikat (keep=False):\n", df.duplicated(keep=False))

# Menghapus duplikat
print("Hapus duplikat (keep first):\n", df.drop_duplicates())
print("Hapus duplikat (keep last):\n", df.drop_duplicates(keep="last"))
print("Hapus semua duplikat (keep=False):\n", df.drop_duplicates(keep=False))

# === SPLIT KOLOM RoleDetail ===
print("Split 'RoleDetail' berdasarkan '_' (tanpa limit):\n", df["RoleDetail"].str.split("_"))
print("Split dan expand ke kolom:\n", df["RoleDetail"].str.split("_", expand=True))
print("Split dengan limit 1:\n", df["RoleDetail"].str.split("_", expand=True, n=1))

# === Memasukkan hasil split ke kolom baru ===
df[["Role", "RoleType"]] = df["RoleDetail"].str.split("_", expand=True)

# Cek hasil akhir
print("Data setelah split dan update kolom Role dan RoleType:\n", df)
