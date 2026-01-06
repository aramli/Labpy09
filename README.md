# Praktikum 9
Tugas Pemrograman Dasar Pertemuan Ke 14 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Tugas Studi Kasus Validasi Data
<ul>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy09/raw/main/img/1.png" width="750"/>
  <li>Hasil Program</li>
  <img src="https://github.com/aramli/labpy09/raw/main/img/2.png" width="750"/><br>
  <img src="https://github.com/aramli/labpy09/raw/main/img/3.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy09/raw/main/img/4.png" width="850"/><br>
  1. Pertama-tama, Kode berfungsi untuk meminta memasukan 3 data, yaitu nama lengkap, nomor telepon, dan email yang tiap inputan nya di simpan pada variable masing masing.
<br><br>

 <img src="https://github.com/aramli/labpy09/raw/main/img/5.png" width="850"/><br>
  2. Selanjutnya, kode variable merupakan list kosong yang nanti nya berfungsi untuk menampung kesalahan jika ada input yang tidak sesuai aturan
<br><br>

<img src="https://github.com/aramli/labpy09/raw/main/img/6.png" width="850"/><br>
  3. Kemudian, Validasi Nama dimana "full_name.replace(" ", "")" berfungsi untuk menghapus spasi dari nama agar tidak dianggap sebagai karakter non-huruf, isalpha() mengecek apakah seluruh karakter adalah huruf.Jika ada karakter selain huruf (misalnya angka atau simbol), maka pesan kesalahan ditambahkan ke list validation_errors.
<br><br>

<img src="https://github.com/aramli/labpy09/raw/main/img/7.png" width="850"/><br>
  4. Lalu, Validasi Nomor telepon, isdigit() mengecek apakah seluruh karakter dalam string adalah angka.Jika ada huruf atau simbol lain, maka dianggap salah dan pesan kesalahan ditambahkan ke list validation_errors.
<br><br>

<img src="https://github.com/aramli/labpy09/raw/main/img/8.png" width="850"/><br>
  5. Lalu, Program mengecek apakah email yang telah di inputkan mengandung tanda @ dan (.) titik, Jika salah satu tidak ada, maka email dianggap tidak valid dan pesan kesalahan ditambahkan.
<br><br>

<img src="https://github.com/aramli/labpy09/raw/main/img/9.png" width="850"/><br>
  6. Terakhir, Pengkondisian Hasil Validasi dimana "len(validation_errors)" menghitung jumlah kesalahan. Jika tidak ada kesalahan (len == 0), maka program menampilkan pesan bahwa data valid.Jika ada kesalahan, program menampilkan semua pesan kesalahan satu per satu dengan perulangan for.
<br><br>


