# minpro-pengecekan kelayakan donor darah
**Nama** : Charist Evlyn Myscha Rerung  
**NIM**  : 25091116102  
**Kelas/Mata Kuliah** : C / Praktikum Dasar-Dasar Pemrograman  

# 1. Flowchart minpro-pengecekan kelayakan donor darah
<img width="1531" height="311" alt="ddpminpro drawio (1)" src="https://github.com/user-attachments/assets/cdc942e7-b423-4439-8d8b-e872a2da6dad" />

# 2. Output Menu
<img width="1920" height="231" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/a9e9d7cb-0928-4df3-be69-db9f4672ffe1" />
Program Kelayakan Donor Darah ini jika dijalankan akan menampilkan menu utama yang terdiri dari 3 pilihan. Menu ini dibuat agar pengguna dapat dengan mudah memilih apa yang ingin dilakukan terkait data pendonor darah.

1.Tambah Data Pendonor\
Pilihan ini digunakan untuk memasukkan data baru pendonor ke dalam sistem.

2.Lihat Data Pendonor\
Menu ini digunakan untuk menampilkan daftar data pendonor yang sudah pernah dimasukkan sebelumnya melalui menu pertama\.

3.Keluar\
Menu terakhir berfungsi untuk mengakhiri program.

**1. tambah data pendonor**
<img width="1920" height="314" alt="donordarahFIXX py - Visual Studio Code 14_09_2025 20_54_04" src="https://github.com/user-attachments/assets/7eb065e0-88db-44f3-8c58-cb55b4375b0c" />
Ketika pengguna memilih menu nomor 1, maka program akan masuk ke bagian input data pendonor baru. Pada tahap ini, sistem meminta beberapa informasi penting dari calon pendonor untuk menentukan apakah orang tersebut layak atau belum layak melakukan donor darah. Alurnya seperti berikut:\

1. Input Nama Pendonor
 - Program akan meminta pengguna untuk mengetikkan nama.
 - Nama ini lah yang digunakan sebagai identitas utama pendonor, sehingga hasil pemeriksaan bisa dicatat sesuai orangnya.

2. Input Umur Pendonor
- Setelah nama, pengguna akan diminta memasukkan umur (tahun)
- Program kemudian akan mengecek apakah umur tersebut memenuhi syarat minimal, yaitu 17 tahun.
- Jika usia masih di bawah 17 tahun, maka otomatis status pendonor dinyatakan “Belum Layak Donor Darah”.

3. Input Berat Badan
- Selanjutnya, program akan meminta pengguna memasukkan berat badan (Kg).
- Berat badan minimal yang diperbolehkan untuk donor adalah 45 Kg.
- Jika berat badan kurang dari 45 Kg, maka hasil pemeriksaan akan menunjukkan status “Belum Layak Donor Darah”.

4. Input Golongan Darah
- Program kemudian meminta pengguna untuk memasukkan golongan darah (A, B, AB, atau O).
- Informasi ini tidak digunakan untuk menentukan kelayakan donor (syarat utama tetap umur dan berat badan), tetapi tetap dicatat sebagai data tambahan.
- Golongan darah ini penting karena dalam dunia nyata sangat dibutuhkan untuk pencocokan antara pendonor dan penerima darah.

5. Proses Pemeriksaan Kelayakan
- Setelah semua data dimasukkan, program akan otomatis menjalankan logika pemeriksaan:
   - Jika umur ≥ 17 tahun dan berat badan ≥ 45 Kg, maka status = Layak Donor Darah.
   - Jika salah satu syarat tidak terpenuhi, maka status = Belum Layak Donor Darah.
 
6. Menampilkan Hasil Pemeriksaan
- Program langsung menampilkan hasil berupa ringkasan data pendonor yang baru saja diinput, seperti:
 Nama\
 Umur\
 Berat badan\
 Golongan darah\
 Status kelayakan\
 Contoh output yang muncul di terminal:
<img width="1920" height="229" alt="donordarahFIXX py - Visual Studio Code 14_09_2025 20_53_09" src="https://github.com/user-attachments/assets/75610c08-41b3-422d-83d3-647864d60c82" />

**2. Lihat data pendonor**
<img width="1920" height="202" alt="donordarahFIXX py - Visual Studio Code 14_09_2025 21_19_58" src="https://github.com/user-attachments/assets/3f5ad3e0-1534-42f9-a027-64b63eeefcee" />
Ketika pengguna memilih menu nomor 2, program akan menampilkan data semua pendonor yang sudah pernah dimasukkan melalui menu Tambah Data Pendonor. Menu Lihat Data Pendonor sangat penting karena berfungsi sebagai output hasil pemeriksaan. Dengan menu ini, pengguna jadi bisa memastikan data yang sudah dimasukkan benar dan sesuai. Namun Jika ada kesalahan, pengguna bisa menambahkan ulang data dengan menu 1

1. Pengecekan Data Pendonor
- Program terlebih dahulu mengecek apakah pendonor berisi data atau masih kosong.
- Jika pendonor masih kosong (belum ada data yang diinput melalui menu 1), maka program tidak bisa menampilkan data.
Pada kondisi ini, muncul pesan:
<img width="786" height="122" alt="1" src="https://github.com/user-attachments/assets/9a345162-036b-4515-a50f-198a695cda13" />

2. Menampilkan Data Jika Sudah Ada\
Jika sudah ada data, maka program akan menampilkan daftar pendonor yang tersimpan.
Data yang ditampilkan meliputi:
Nama\
Umur\
Berat badan\
Golongan darah\
Status kelayakan donor
<img width="352" height="163" alt="4" src="https://github.com/user-attachments/assets/a7babda6-19b3-40ab-bd93-b1e3bffca46a" />

**3. Keluar**\
<img width="812" height="61" alt="5" src="https://github.com/user-attachments/assets/f4ce6539-f52c-42b8-a8b5-2820d7972922" />\
Menu ini berfungsi sebagai exit point dari program.\
Dengan adanya menu keluar, pengguna tidak perlu menutup terminal secara paksa, melainkan bisa mengakhiri program dengan cara yang benar.
Menu Keluar adalah pilihan terakhir dari program. Jika pengguna memilih angka 3 pada menu utama, maka program akan segera menghentikan proses dan menampilkan pesan perpisahan kepada pengguna.


