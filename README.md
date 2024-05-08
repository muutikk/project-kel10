# Project Kelompok 10
## Overview
Ini adalah sebuah project untuk melakukan ETL sederhana. project ini mencakup hal-hal sebagai berikut:
1. Bahasa pemrograman Python
2. Docker
3. PostgreSQL

## Pembuatan Data Dummy
  Untuk membuat data dummy kami menggunakan library pandas dan random. Data yang kami buat merupakan data production dan sales dari sebuah pabrik mainan. kami menggunakan function production_and_sales_data untuk membuat datanya. dimana didalamnya kami membuat data dengan kolom-kolom sebagai berikut :
  - tahun produksi
  - bulan produksi
  - mainan
  - produksi
  - penjualan
  - harga satuan
  - pendapatan

  selanjutnya Data dummy yang dihasilkan kemudian dikonversi menjadi DataFrame Pandas menggunakan fungsi pd.DataFrame(data) dan disimpan dalam format csv.

## ETL (Extract, Transform, Load)
Berikut adalah langkah-langkah yang digunakan dalam proses ETL(Extract, Transform, Load) :
### Extract
  Tahap Extract digunakan untuk mengambil data dari sumber data. Karena dalam project ini kami hanya memiliki satu format data, maka kami hanya menggunakan library pandas untuk mengekstrak data dari file CSV ke dalam data frame dan menampilkan datanya.
### Transform
  Pada tahap transformasi ini, kami menggunakan Python untuk mentransformasi data sesuai kebutuhan kami, yang kami lakukan adalah:
  1. Menghapus missing value menggunakan df.dropna(inplace=True)
  2. Menambahkan kolom sisa produksi dengan melakukan pengurangan antara kolom produksi dan penjualan (Produksi - Penjualan)
  3. Mengeliminasi baris data dimana jumlah penjualan lebih besar dari jumlah produksi (Penjualan > Produksi)
### Load
  Tahap Load digunakan untuk memuat data yang telah ditransformasikan ke dalam gudang data atau basis data. Dalam hal ini, kami menggunakan PostgreSQL dengan Docker image. Saya menggunakan psycopg2 untuk membantu saya menghubungkan Python dengan PostgreSQL.
  


