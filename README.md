# 0/1 Knapsack Problem - Backtracking (KAI Cargo Optimization)

Repositori ini berisi implementasi algoritma **Backtracking** dalam bahasa Python untuk menyelesaikan persoalan optimasi pengangkutan barang (0/1 Knapsack Problem).

## Deskripsi Masalah
Program mencari kombinasi muatan kereta api yang memberikan keuntungan (*profit*) maksimal dengan batasan kapasitas tertentu. 

**Parameter Persoalan:**
* **Kapasitas Maksimal:** 10 Ton
* **Jumlah Item:** 10 (Semen, Baja Ringan, Beras, Pupuk, Gula, dll.)
* **Metode:** Backtracking dengan *Pruning* (pemangkasan cabang yang melebihi kapasitas).

## Logika Program
Program menggunakan fungsi rekursif untuk mengevaluasi setiap item dengan dua opsi keputusan:
1. **Ambil Item ($x_i=1$):** Dilakukan hanya jika total berat tidak melebihi kapasitas (Constraint).
2. **Tidak Ambil Item ($x_i=0$):** Melanjutkan pencarian ke item berikutnya.

Jika ditemukan kombinasi dengan profit yang lebih tinggi dari sebelumnya, program akan memperbarui nilai optimalnya.

## Cara Menjalankan
Pastikan Anda memiliki Python terinstal, lalu jalankan:
```bash
program.py
