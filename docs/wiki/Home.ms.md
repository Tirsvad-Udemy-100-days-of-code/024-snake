> Halaman ini dijana daripada README.md dan wiki/. Perubahan di sini akan ditimpa apabila wiki diterbitkan lagi.

> Halaman Bahasa Inggeris adalah yang rasmi; terjemahan ini mengikutinya.

[English](Home) | [Dansk](Home.da) | Bahasa Melayu

# Permainan Ular (hari 24)

Permainan Ular (Snake) klasik, dibina dengan modul `turtle` Python. Ia ialah tugasan hari ke-24 dalam *100 Days of Code: The Complete Python Pro Bootcamp* di Udemy, yang mengajar sistem fail setempat serta cara membaca dan menulis fail. Seekor ular bergerak sendiri merentasi skrin hitam 600 kali 600 dan dikawal dengan kekunci anak panah; ia makan makanan dan membesar, dan papan skor di bahagian atas memaparkan skor serta skor tertinggi. Permainan tidak tamat: apabila kepala melepasi dinding atau menyentuh ekornya sendiri, ular dan skor bermula semula, dan skor terbaik disimpan dalam fail `data.txt`, jadi ia masih ada apabila anda bermain lagi.

![Permainan pada skor 5 dengan skor tertinggi 12: seekor ular hijau muda dengan kepala hijau tua dan mulut, makanan biru dan skor di bahagian atas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/raw/branch/main/docs/images/snake-score-5.png)

*Permainan yang sedang berjalan pada skor 5 dengan skor tertinggi 12: badan hijau muda, kepala hijau tua dengan mulut, makanan biru dan papan skor putih.*

## Kawalan

| Kekunci | Kesan |
| --- | --- |
| Atas, Bawah, Kiri, Kanan | Memusingkan ular |

Ular tidak pernah berpusing terus ke belakang ke atas dirinya sendiri. Apabila kepala menghampiri makanan biru dalam jarak kurang daripada 15 piksel, ular memakannya, bertambah panjang satu segmen dan skor naik 1.

## Fail skor tertinggi

Skor tertinggi disimpan sebagai teks dalam `data.txt` di folder tempat anda memulakan permainan. Fail itu dicipta dengan nilai `0` kali pertama. Untuk bermula dari sifar semula, tutup permainan dan padam fail itu.

## Jalankan

Python 3.13 atau lebih baharu dengan `tkinter` diperlukan; permainan ini tiada kebergantungan lain semasa dijalankan.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake.git
cd 024-snake
python -m pip install -e .
python -m snake_game
```

README repositori mempunyai persediaan penuh untuk Windows, Linux dan macOS.
