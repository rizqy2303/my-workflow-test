import pandas as pd
import numpy as np
import os  

input_data_path = "namadataset_raw/train.csv"

output_dir = "preprocessing/namadataset_preprocessing"
output_data_path = os.path.join(output_dir, "train_cleaned.csv")

os.makedirs(output_dir, exist_ok=True)
print(f"Memulai proses data loading dari: {input_data_path}")
try:
    df = pd.read_csv(input_data_path)
    print("Data loading berhasil.")
except FileNotFoundError:
    print(f"ERROR: File tidak ditemukan di {input_data_path}")
    print("Pastikan file 'train.csv' ada di dalam folder 'namadataset_raw'.")
    exit() 

print("Memulai proses data preprocessing...")

df['Age'] = df['Age'].fillna(df['Age'].mean())

if 'Cabin' in df.columns:
    df = df.drop('Cabin', axis=1)

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("Proses preprocessing selesai.")
print(f"Menyimpan data bersih ke: {output_data_path}")
try:
    df.to_csv(output_data_path, index=False)
    print("Data bersih berhasil disimpan.")
    print("--- SEMUA PROSES SELESAI ---")
except Exception as e:
    print(f"ERROR: Gagal menyimpan file. {e}")