# MINI_PROJECT - "PROGRAM KELAYAKAN DONOR DARAH"
# Nama : Charist Evlyn Myscha Rerung
# NIM  : 25091116102
# Kelas/Mata Kuliah : C/Praktikum Dasar-Dasar Pemrogram

pendonor = []

print("PROGRAM KELAYAKAN DONOR DARAH")
print("Menu")
print("1. Tambah Data pendonor")
print("2. Lihat Data Pendonor")
print("3. Keluar")

pilihan = int(input("Pilih Menu (1-3):"))

if pilihan == 1:
   print("Tambah Data Pendonor")
   nama = input("Masukkan nama pendonor:")
   umur = int(input("Masukkan umur:"))
   berat = int(input("Masukkan berat badan (Kg):"))
   golongan = input("Masukkan golongan:")

   if umur >= 17 and berat >= 45:
      status = "layak donor darah"
   else:
      status = "Belum layak donor darah"

   print("Pendonor atas nama", nama, "dengan umur", umur, "Tahun dan berat", berat, "Kg dengan golongan darah", golongan, status)

   data1 = (nama, umur, berat, golongan, status)
   pendonor = [data1]
      
   print("\n=====Hasil Pemeriksaan Donor Darah=====")
   print("Nama:", pendonor [0][0])
   print("umur:", pendonor [0][1], "tahun")
   print("berat:", pendonor [0][2], "Kg")
   print("golongan:", pendonor [0][3])
   print("status:", pendonor [0][4])

   print("\n======TERIMAKASIH, SELALU JAGA KESEHATAN YAAA!!:)=========")

if pilihan == 2:  
   if pendonor :
       print("\n====== Data Pendonor ======")
       data = pendonor [0]
       print("nama:", data [0])
       print("umur:", data [1], "Tahun")
       print("berat:", data [2], "Kg")
       print("golongan:", data[3])
       print("status:", data [4])
   else:
       print("Yahhh belum ada daftar pendonor nih, Silahkan isi menu 1 dulu yaaa.")
     
elif pilihan == 3:
     print("sippppp, makasih udah pakai program ini! sehat dan semangat selalu yaa!!")


print("\nPROGRAM KELAYAKAN DONOR DARAH")
print("Menu")
print("1. Tambah Data pendonor")
print("2. Lihat Data Pendonor")
print("3. Keluar")

pilihan = int(input("Pilih Menu (1-3):"))

if pilihan == 1:
   print("Tambah Data Pendonor")
   nama = input("Masukkan nama pendonor:")
   umur = int(input("Masukkan umur:"))
   berat = int(input("Masukkan berat badan (Kg):"))
   golongan = input("Masukkan golongan:")

   if umur >= 17 and berat >= 45:
      status = "layak donor darah"
   else:
      status = "Belum layak donor darah"

   print("Pendonor atas nama", nama, "dengan umur", umur, "Tahun dan berat", berat, "Kg dengan golongan darah", golongan, status)

   data1 = (nama, umur, berat, golongan, status)
   pendonor = [data1]
      
   print("=====Hasil Pemeriksaan Donor Darah=====")
   print("Nama:", pendonor [0][0])
   print("umur:", pendonor [0][1], "tahun")
   print("berat:", pendonor [0][2], "Kg")
   print("golongan:", pendonor [0][3])
   print("status:", pendonor [0][4])

   print("======TERIMAKASIH, SELALU JAGA KESEHATAN YAAA!!:)=========")

if pilihan == 2:  
   if pendonor :
       print("\n====== Data Pendonor ======")
       data = pendonor [0]
       print("nama:", data [0])
       print("umur:", data [1], "Tahun")
       print("berat:", data [2], "Kg")
       print("golongan:", data[3])
       print("status:", data [4])
   else:
       print("Yahhh belum ada daftar pendonor nih, Silahkan isi menu 1 dulu yaaa.")
      
elif pilihan == 3:
     print("sippppp, makasih udah pakai program ini! sehat dan semangat selalu yaa!!")


