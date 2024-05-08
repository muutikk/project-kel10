import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

user = 'postgres'
password = 'postgres'
hostname = '127.0.0.1'
database = 'postgres'
port = '5436'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine = create_engine(conn_string)
conn = engine.connect()

# Fungsi untuk mengekstrak data dummy
def ekstrak(url):
    df = pd.read_csv(url)
    return df

# Fungsi untuk melakukan transformasi data
def transform_data(df):
    # Menghapus nilai NULL
    df.dropna(inplace=True)

    # Menambahkan kolom sisa produksi
    df['Sisa Produksi'] = df['Produksi'] - df['Penjualan']

    # Menghapus baris dimana nilai penjualan lebih besar dari produksi
    df = df[df['Penjualan'] <= df['Produksi']]

    return df

# Fungsi untuk memuat data yang telah ditransformasi ke dalam PostgreSQL
def load(df, table_name):
    # Menuliskan dataframe ke dalam tabel di PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Ekstrak data dummy
file_dir = 'https://raw.githubusercontent.com/muutikk/project-kel10/main/Data_Dummy/Production_and_Sales.csv'
df = ekstrak(file_dir)

# Transformasi data
df = transform_data(df)

# Simpan file transformasi sebagai CSV jika perlu
transformed_filename = 'Transformed_Production_and_Sales.csv'
df.to_csv(transformed_filename, index=False)
print("Data telah di-transform dan disimpan sebagai '{}'.".format(transformed_filename))

# Memuat data yang telah ditransformasi ke dalam PostgreSQL
table_name = 'production_and_sales_transformed'
load(df, table_name)
print("Data telah dimuat ke dalam tabel '{}' di PostgreSQL.".format(table_name))
