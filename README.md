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
### Spesifikasi minimum
* Android version : Lollipop v5.x or above
* Storage required : 25 MB

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
#### Case : Random Word dan Referensi Lagu
![randoman-Random Word+Lagu](https://user-images.githubusercontent.com/78886557/120921939-858d1b00-c6f0-11eb-8bd9-2013a152126c.png)
#### Case : Random Word dan Tulis Diary
![randoman-Random Word+Diary](https://user-images.githubusercontent.com/78886557/120921940-8756de80-c6f0-11eb-8e41-1bd00df54907.png)
#### Case : Tulis Diary
![randoman-Tulis Diary](https://user-images.githubusercontent.com/78886557/120921945-8aea6580-c6f0-11eb-81ff-fe16a5e414d5.png)
#### Case : Buka History Diary
![randoman-History Diary](https://user-images.githubusercontent.com/78886557/120921941-87ef7500-c6f0-11eb-8e8c-13c4f9c4a50a.png)
#### Case : Buka Settings
![randoman-Kelola Pin](https://user-images.githubusercontent.com/78886557/120921943-88880b80-c6f0-11eb-8a17-78103dec37ac.png)

### Class Diagram
![AAAAAK](https://user-images.githubusercontent.com/67861610/120893365-20c4b880-c63d-11eb-801b-0534c68ab800.png)
### Entity Relationship Diagram
![ERD Diagram](https://user-images.githubusercontent.com/67861610/120893383-46ea5880-c63d-11eb-901e-f3e5d1faea5b.png)
### Schematic Diagram
![Schematic Diagram](https://user-images.githubusercontent.com/78713771/122032703-143d1e80-cdfa-11eb-9854-91a2690b5ebd.png)
### Arsitektur Sistem
![activity-diag](https://user-images.githubusercontent.com/78886557/120140575-09349c80-c205-11eb-9e96-76fca9911464.png)
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
![CollageMaker_20210605_153634358](https://user-images.githubusercontent.com/67861610/120893443-8fa21180-c63d-11eb-8a93-142de4e0cd73.jpg)
![CollageMaker_20210605_153653899](https://user-images.githubusercontent.com/67861610/120893440-8c0e8a80-c63d-11eb-92a1-8d65f1c5f4ed.jpg)
![CollageMaker_20210605_153718520](https://user-images.githubusercontent.com/67861610/120893434-8749d680-c63d-11eb-802a-a6d294beb311.jpg)
![CollageMaker_20210605_153756182](https://user-images.githubusercontent.com/67861610/120893418-76996080-c63d-11eb-9c71-2b81cf8c612c.jpg)
![CollageMaker_20210605_153813608](https://user-images.githubusercontent.com/67861610/120893427-82852280-c63d-11eb-97f3-8898db8c781b.jpg)

### Proses Implementasi Database
1. Create Table Word

CREATE TABLE Word(kondisi VARCHAR(5), teks VARCHAR(500));

2. Input Data Table Word

INSERT INTO Word VALUES('sedih', 'Percayalah bahwa Tuhan selalu adil. Dalam setiap kesedihan pasti akan muncul kebahagiaan.');

INSERT INTO Word VALUES('sedih', 'Percayalah kau masih bisa menjadi orang yang lebih baik dari kemarin. Kau berharga dan berhak bahagia.');

INSERT INTO Word VALUES('sedih', 'Sejatinya, kesedihan adalah sebuah pengalaman yang mengajarkan untuk menjadi kuat. Jangan patah semangat untuk kamu yang masih berjuang!');

INSERT INTO Word VALUES('sedih', 'Tuhan tidak pernah terlambat. Tuhan tau perjuanganmu. Ada saatnya penderitaanmu akan diubah menjadi sukacita. Percayalah :D');

INSERT INTO Word VALUES('sedih', 'Saat dunia ini memiliki 100 alasan buatmu bersedih, ingatlah bahwa Tuhan memiliki takhingga alasan untuk tetap membuatmu tersenyum. May you always have a smile on your face.');

INSERT INTO Word VALUES('sedih', 'Apa yang kamu harapkan belum tentu baik untukmu, tetapi Tuhan pasti memberikan yang terbaik.');

INSERT INTO Word VALUES('sedih', 'Teruslah berjuang! Kamu tak akan pernah tahu hasil dari perjuanganmu jika kamu berhenti berjuang.');

INSERT INTO Word VALUES('sedih', 'Tuhan selalu punya cara indah untuk membuat hamba-Nya bangkit dan tersenyum meski dalam tangis sekalipun.');

INSERT INTO Word VALUES('sedih', 'Semua yang berharga pasti butuh diperjuangkan, janganlah patah semangatmu, ada upah bagi kerja keras dan air matamu.');

INSERT INTO Word VALUES('marah', 'Siapa lekas naik darah, berlaku bodoh, tetapi orang yang bijaksana, bersabar.');

INSERT INTO Word VALUES('marah', 'Berhentilah marah dan tinggalkan panas hati itu, jangan marah, itu hanya membawa kepada kejahatan.');

INSERT INTO Word VALUES('marah', 'Orang bebal melampiaskan seluruh amarahnya, tetapi orang bijaksana meredakannya.');

INSERT INTO Word VALUES('marah', 'Jangan mudah terpancing emosi oleh orang lain, tetapi berikanlah senyuman kepadanya.');

INSERT INTO Word VALUES('marah', 'Tenangkan diri, karena amarah akan membuat kamu tidak bisa berpikir dengan tenang.');

INSERT INTO Word VALUES('marah', 'Manusia hebat adalah manusia yang bisa mengendalikan diri saat dikuasai amarah, tenang saat dipermalukan, dan tersenyum saat diremehkan.');

INSERT INTO Word VALUES('marah', 'Betapa jauh lebih menyedihkan akibat dari kemarahan daripada penyebabnya.');

INSERT INTO Word VALUES('marah', 'Kemarahan adalah tanda bahwa sesuatu perlu diubah.');

INSERT INTO Word VALUES('sakit', 'Semua orang berjuang untuk melawan sesuatu. Nah, kamu sedang melawan sakit, jadi bersemangatlah!');

INSERT INTO Word VALUES('sakit', 'Sakit ini bukan penghalang untukmu. Kamu harus percaya bisa melewati semuanya ya.');

INSERT INTO Word VALUES('sakit', 'Kamu itu orang yang kuat, jadi aku yakin kamu bisa cepat sembuh.');

INSERT INTO Word VALUES('sakit', 'Sabar, jangan menyerah, dan terus lawan penyakit itu. Tidak lama lagi kamu akan melihat ke belakang dan bilang, "semuanya sudah kulalui". Aku tahu kamu pasti bisa, karena kamu kuat.');

INSERT INTO Word VALUES('sakit', 'Mungkin ini adalah cara Tuhan membersihkan dosamu. Bersabarlah sedikit lagi, kamu akan segera sembuh.');

INSERT INTO Word VALUES('sakit', 'Kita tidak akan tahu indahnya sembuh sampai kita merasakan sakit.');

INSERT INTO Word VALUES('sakit', 'Kegelisahan adalah separuh penyakit, ketenangan adalah separuh obat, dan kesabaran adalah awal kesembuhan.');

INSERT INTO Word VALUES('sakit', 'Hati yang gembira adalah obat.');

INSERT INTO Word VALUES('galau', 'One day that name will not make you smile anymore. Those memories will not make you cry anymore. Do not worry, you will heal. It will take time, but you will surely heal.');

INSERT INTO Word VALUES('galau', 'Even though you are heartbroken, keep your heart open, so pain can find an exit.');

INSERT INTO Word VALUES('galau', 'Your softness is so beautiful. Please do not let heartbreak take that from you.');

INSERT INTO Word VALUES('galau', 'Do not cry too much. Turn heartbreak into kindness. Search for healing words and plant them into your wounds. One day, you will have a garden of love.');

INSERT INTO Word VALUES('galau', 'I believe you will survive many near-deaths of your soul, but you must stand up, overcome the wounds of your heart, rise from ashes, and go on with your life.');

INSERT INTO Word VALUES('galau', 'It is okay if you thought you were over it, but it hits you all over again. It is okay to fall apart even if you thought you had it under control. You are not weak. Healing is messy and there is no timeline for healing.');

INSERT INTO Word VALUES('galau', 'This is how you love yourself. Instead of begging for the pain to go away, you choose to hear what your pain is begging of you and to make peace with your pain.');

3. Create Table Lagu

CREATE TABLE Lagu(kondisi VARCHAR(10), link VARCHAR(40), judul VARCHAR(200));

4. Input Data Table Lagu

INSERT INTO Lagu VALUES('sedih','https://youtu.be/0FiJfOviW4U ','Membasuh - Hindia');

INSERT INTO Lagu VALUES('sedih','https://youtu.be/k4V3Mo61fJM ','Fix you - Coldplay');

INSERT INTO Lagu VALUES('sedih','https://youtu.be/nkJnteauOAY ','Sudah - Ardhito Pramono');

INSERT INTO Lagu VALUES('sedih','https://youtu.be/L2XSg_8vNBE ','Pelukku Untuk Pelikmu - Fiersa Bersari');

INSERT INTO Lagu VALUES('sedih','https://youtu.be/qCN8tdHbs8c ','Lekas-Tulus');

INSERT INTO Lagu VALUES('sedih','https://youtu.be/kcc9Kfip2uw ','Secukupnya - Hindia');

INSERT INTO Lagu VALUES('marah','https://youtu.be/kHue-HaXXzg ','Let It Go - Demi Lovato');

INSERT INTO Lagu VALUES('marah','https://youtu.be/_WyLVrtLhvk ','Ya Sudahlah - Bondan Prakoso, Fade2Black');

INSERT INTO Lagu VALUES('marah','https://youtu.be/HHP5MKgK0o8 ','Kill em With Kindness - Selena Gomez');

INSERT INTO Lagu VALUES('marah','https://youtu.be/L2XSg_8vNBE ','Pelukku Untuk Pelikmu - Fiersa Bersari');

INSERT INTO Lagu VALUES('marah','https://youtu.be/2vjPBrBU-TM ','Chandelier - Sia');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/Mgfe5tIwOj0 ','IDGAF - Dua Lipa');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/k2qgadSvNyU ','New Rules - Dua Lipa');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/EEhZAHZQyf4 ','Thank You, Next - Ariana Grande');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/WA4iX5D9Z64 ','We Are Never Ever Getting Back Together - Taylor Swift');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/V-iqU4keqq0 ','Sudahkah? - Eclat');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/YncQyAb1xBQ ','Lapang Dada - Sheila On 7');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/lu1b04XPQv0 ','Untuk Hati Yang Terluka - Isyana Sarasvati');

INSERT INTO Lagu VALUES('patah hati','https://youtu.be/MV_euZ_lKH8 ','Jodoh Pasti Bertemu - Afgan');

5. Create Table Diary

CREATE TABLE Diary(tanggal VARCHAR(10), textdiary VARCHAR(5000), judul VARCHAR(100));

6. Create Table Pin

CREATE TABLE Pin(userpin VARCHAR(15), pertanyaan VARCHAR(50), jawaban VARCHAR(50));

### Link Aplikasi
Klik [di sini](https://drive.google.com/file/d/1kCx_L1CYJtuA3CBmNrAl_SUTElo3Clz3/view?usp=drivesdk) untuk mendapatkan aplikasi Wordiary.

## Testing (Test Case)
### Positive Case and Negative Case
![Screenshot (349)](https://user-images.githubusercontent.com/67861610/120895849-0c86b880-c649-11eb-98f4-4fbc717022a6.png)

## Saran untuk Pengembangan Selanjutnya
1. Pengembang selanjutnya dapat melakukan penyempurnaan ukuran tombol emotikon agar pada setiap perangkat memiliki ukuran yang sama.
2. Pengembang selanjutnya dapat membuat UI/UX yang lebih menarik lagi agar lebih berwarna dan tidak membosankan.
3. Pengembang selanjutnya dapat men-deploy aplikasi untuk iOS.

## Dokumentasi
* [Trello](https://trello.com/b/hXKCDk7k/wordiary)
* [Github](https://github.com/willy07pr/Wordiary)
* [Google Sites](https://sites.google.com/view/wordiary/journal)
