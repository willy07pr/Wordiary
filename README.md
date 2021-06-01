# Laporan Akhir Proyek Rekayasa Perangkat Lunak
![1](https://user-images.githubusercontent.com/78713780/119604362-1cb4c180-be19-11eb-929d-b0606a8c233c.png)
## Paralel 1
## Kelompok 14
## Asisten Praktikum
1. Indah Puspita (G64170035)
2. Qoriatul Khairunnisa (G64170014)
## WiiDev-Team
1. Ivana (G54190055) - Project Leader, Back-end Developer, UI/UX Designer
2. Vindyani (G54190027) - Back-end Developer, UI/UX Designer
3. Denny Muliawan Sebastian (G54190007) - Front-end Developer, UI/UX Developer
4. Willy Pratama (G54190029) - Front-end Developer, UI/UX Developer

## Deskripsi Singkat Aplikasi Wordiary
Pada masa pandemi, stress semakin sering dialami karena khawatir berlebihan dan merasa sendirian. Oleh sebab itu, aplikasi yang memiliki tempat curhat dan penyemangat dibutuhkan oleh banyak orang. Aplikasi "Wordiary" hadir menjadi salah satu solusi masalah ini.

Aplikasi "Wordiary" merupakan aplikasi mobile berbasis android. Aplikasi ini ditargetkan untuk pengguna yang dirasa sulit untuk mencurahkan isi hatinya ke orang lain sehingga si pengguna dapat menggunakan fitur buku harian (note) yang disediakan pada aplikasi ini sebagai gantinya, baik ketika suasana hatinya sedang baik maupun buruk. Kami juga menargetkan pengguna dengan suasana hati yang sedang buruk dan membutuhkan kata-kata penyemangat juga saran lagu yang mungkin dapat meningkatkan mood atau suasana hati si pengguna.

Tujuan utama dari pengembangan aplikasi ini adalah membantu pengguna meningkatkan mood mereka dengan fitur-fitur yang tersedia.

## User Analysis
### User Stories
#### Nice-to-develop
1. Sebagai pengguna yang lupa pin, agar dapat masuk aplikasi, saya dapat menggunakan fitur lupa pin.
2. Sebagai pengguna fitur diary, agar privasi saya terlindungi, saya dapat menetapkan nomor pin kunci aplikasi.
3. Sebagai pengguna yang ingin melindungi mata, agar layar aplikasi yang dilihat tidak terlalu mencolok, saya dapat mengaktifkan fitur dark mode.
4. Sebagai pengguna yang membutuhkan media yang dapat mengalihkan amarah/rasa sedih/sakit hati/pikiran negatif ketika sedang sakit, saya dapat memilih tombol emotikon yang sesuai dengan kondisi hati saya agar mendapatkan referensi lagu yang cocok untuk mengalihkan kondisi hati saya saat itu.
#### Need-to-develop
5. Sebagai pengguna yang telah membuat diary, agar dapat membaca ulang diary yang telah dibuat, saya dapat menggunakan fitur history untuk memilih tanggal penulisan diary.
6. Sebagai pengguna yang sedang marah, agar amarah saya dapat diredam, saya dapat membuka fitur kata-kata penyemangat dengan menekan tombol emotikon 'marah'.
7. Sebagai pengguna yang sedang sedih, agar kesedihan dapat dihibur dan semangat kembali, saya dapat memilih tombol emotikon 'sedih' pada aplikasi Wordiary.
8. Sebagai pengguna yang sedang patah hati, saya dapat memilih tombol emotikon 'patah hati' agar dapat meringankan rasa sakit hati saya.
9. Sebagai pengguna yang sedang sakit, saya dapat memilih tombol emotikon 'sakit' agar dapat terus memiliki mindset positif ketika sedang sakit.
10. Sebagai pengguna yang ingin curhat, agar dapat mencurahkan semua isi hati saya, saya dapat menggunakan fitur diary untuk menuliskan unek-unek yang saya miliki.

## Spesifikasi Teknis Lingkungan Pengembangan
### Perangkat Keras
* Processor     : Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz (4 CPUs), ~2.4GHz 
* Memory        : 8192 MB RAM
* Graphics Card : Intel(R) HD Graphics 4400
* Storage       : 256 GB
### Perangkat Lunak
* Operating System        : Windows 10
* Text Editor 			      : Pycharm Edu
* Framework			          : Kivy, KivyMD
* Database			          : SQLite
* Library				          : Kivy Library
* Version Control System 	: Github
* Deployment			        : Buildozer, Virtual Box for Linux
* Lain-lain			          : SQLite3 (Adapter database to py)

## Hasil dan Pembahasan
### Use Case Diagram
![WhatsApp Image 2021-05-31 at 11 50 42](https://user-images.githubusercontent.com/78886557/120141328-7bf24780-c206-11eb-8ba7-a8a4b8a8e7fc.jpeg)
### Activity Diagram
![activity-diag](https://user-images.githubusercontent.com/78886557/120140575-09349c80-c205-11eb-9e96-76fca9911464.png)
### Class Diagram
### Entity Relationship Diagram
### Arsitektur Sistem
#### Ringkasan
Untuk menyimpan, mengakses, dan meng-update data, kami memutuskan untuk menggunakan PostgreSQL. Untuk mengakses, meng-update data, merancang, dan memastikan aplikasi dapat berjalan, kami memutuskan untuk menggunakan bahasa pemrograman Python. Untuk merealisasikan UI/UX dari aplikasi, kami memutuskan untuk menggunakan framework Kivy dan library KivyMD. Untuk mengonversi hasil pemrograman menjadi file aplikasi berbasis Android, kami memutuskan untuk menggunakan Buildozer yang berbasis Linux.
#### Masalah
* Pengguna IOS tidak dapat menggunakan aplikasi ini karena aplikasi yang kami buat hanya berbasis Android. Masalah ini penting untuk dipecahkan agar aplikasi ini dapat digunakan khalayak secara lebih luas.
* Proses masuk aplikasi yang memakan waktu karena kodingan yang dibuat belum cukup efisien. Masalah ini penting untuk dipecahkan supaya pengguna dapat merasa lebih nyaman saat menggunakan aplikasi ini.
#### Batasan
* Proyek pengembangan software yang kami buat hanya berfungsi di Android padahal ada klien yang menginginkan untuk menggunakan aplikasi ini di IOS.
* Proses masuk aplikasi yang cukup memakan waktu padahal klien menginginkan aplikasi yang responsif dan cepat. Hal ini terjadi karena penulisan codingan yang tidak efisien.
#### Opsi
##### Klien ingin menggunakan aplikasi ini di IOS.
* Pro : Aplikasi ini dapat menjangkau khalayak secara lebih luas.
* Kontra : Kami belum mengetahui cara mengonversi aplikasi ini dengan basis IOS.
##### Klien menginginkan aplikasi yang responsif dan cepat.
* Pro :
  - Pengguna dapat menggunakan aplikasi ini dengan lebih nyaman.
  - Pengevaluasi codingan akan lebih mudah dilakukan bila codingan ditulis dengan lebih ringkas.
* Kontra :
  - Memakan waktu lebih banyak untuk meringkas codingan yang sebenarnya sudah jadi.
  - Ada kemungkinan terjadinya error setelah codingan tersebut diringkas.
#### Rasional
* Klien ingin menggunakan aplikasi ini di IOS
  - Kami memilih opsi pro dengan beberapa pertimbangan. Apabila dirasa terlalu sulit untuk mengonversi aplikasi ini menjadi berbasis IOS, maka kami putuskan untuk tetap membiarkan aplikasi ini untuk tersedia di Android saja.
* Klien menginginkan aplikasi yang responsif dan cepat
  - Kami memilih opsi pro untuk meningkatkan kenyamanan pengguna dalam menggunakan aplikasi ini sehingga memacu pengguna tersebut untuk menggunakan aplikasi ini dalam jangka waktu yang lama

### Fungsi Utama Yang Dikembangkan
* Fitur Buku Harian
* Fitur Kata-Kata Penyemangat
* Fitur Referensi Lagu
### Fungsi CRUD
#### Create
1. Membuat pin
2. Membuat buku harian
#### Read
1. Mencari riwayat buku harian
2. Membaca kata penyemangat
3. Membaca referensi lagu
#### Update
1. Mengganti pin
2. Mengedit buku harian, 
#### Delete
1. Menghapus pin
2. Lupa pin
## Hasil Implementasi
### Screenshot Sistem
![WhatsApp Image 2021-05-26 at 11 51 32 (2)](https://user-images.githubusercontent.com/78713780/119606498-e711d780-be1c-11eb-828f-470e0f82d729.jpeg)
![WhatsApp Image 2021-05-26 at 11 51 32 (1)](https://user-images.githubusercontent.com/78713780/119606503-e8430480-be1c-11eb-8639-c51d98d16a50.jpeg)
![WhatsApp Image 2021-05-26 at 11 51 32](https://user-images.githubusercontent.com/78713780/119606506-e8db9b00-be1c-11eb-9f11-d08de9412132.jpeg)
![WhatsApp Image 2021-05-26 at 11 51 33 (1)](https://user-images.githubusercontent.com/78713780/119606507-e8db9b00-be1c-11eb-932a-ea0bf28b3cea.jpeg)
![WhatsApp Image 2021-05-26 at 11 51 33](https://user-images.githubusercontent.com/78713780/119606508-e9743180-be1c-11eb-9cac-7ec7b3914725.jpeg)
### Link Aplikasi

## Testing (Test Case)
### Positive Case
### Negative Case

## Saran untuk Pengembangan Selanjutnya

## Spesifikasi minimum
* Android version : Lollipop v5.x or above
* Storage required : 25 MB
