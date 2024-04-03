#1. Identifikasi Masalah.
   
   Dalam perkuliahan, kita tau ada yang namanya jadwal kuliah,waktu dan ruangan yang digunakan.
   kita mungkin akan merasa ribet jika harus harus mencari dan membuka file yang telah di bagikan oleh prodi setiap hari untuk melihat 
   jadwal hari ini.
   
   Ada berbagai cara untuk mnyelesaikan permasalahan ini, salah satu contohnya adalah menulis jadwal dalam kertas lalu menempelkannya 
   pada tempat yang sering kita lihat seperti di tembok kamar. 
   Nah, dari banyaknya cara yang bisa digunakan untuk menyelesaikan permasalahan tersebut, saya menggunakan program python sederhana 
   sebagai sarana penyelesaian .
   kode tersebut merupakan kode python sederhana yang di buat untuk menyelesaikan pemasalahan tersebut dimana algoritma kode tersebut 
   adalah
   
A. Dekarasi Variabel (Bagian Pertama 	Dalam Kode)

   			'''jadwal = {"Senin" : "Matematika diskrit, Jam .........'''

a. jadwal: jadwal disini, merupakan sebuah dictionary(Tipe Data) yang berisi tentang jadwal kuliah untuk setiap harinya, Key / kunci 
   dari Tipe data dictionary tersebutadalah "nama_hari" dan value/ nillai dari dictionary tersebut adalah string yang berisi informasi 
   tentang mata pelajaran, jam, dan ruangan
      
 		  '''input_hari = str(input("Masukan Kata kunci dalam bentuk nama hari (Senin/Selasa dst...): "))'''

b. Input hari: Input hari disini merupakan sebuah variabel string yang digunakan untuk menyimpan nama hari yang di input oleh pengguna

B. Mengambil Input Pengguna (Bagian Kedua Dalam Kode)

      '''input_hari = str(input("Masukan Kata kunci dalam bentuk nama hari (Senin/Selasa dst...): "))'''
   
c. Bagian / baris kedua kode ini merupakan sebuah fungsi dimana fungsi dalam kode ini bertujuan untuk meminta pengguna untuk 
   memasukkan nama hari dan menyimpannya dalam variabel input_hari.

    	'''input_hari = input_hari.capitalize()'''
   
d. Bagian / baris Ke tiga dari kode ini merupakan sebuah fungsi dimana fungsi tersebut digunakan untuk mengonversi input-an string 
   dari pengguna kedalam format Kapitalisasi atau membuat huruf pertama menjadi huruf kapita.

C. Mengambil Value / (Bagaian ketiga Dalam Kode)

   	  	'''jadwal_hari_ini = jadwal.get(input_hari)'''
   
e. Baris ketiga dari kode tersebut merupakan sebuah method "get()" yang digunakan untuk mengambil value / nilai dari dictionary 
  "jadwal" berdasarkan key atau inputan pengguna dalam "input_hari". Jika key / inputan yang dimasukan pengguna tersebut tidak ditemukan, 
   maka method "get()" akan mengembalikan nilai None.
   
D. Menampilkan output berdasarkan key ata inputan pengguna

   	  '''if jadwal_hari_ini:'''
   
   	  '''print(f"Kata kunci hari yang di input adalah {input_hari} , Berdasarkan kata kunci yang di input, jadwal kuliah untuk hari ini 
   	   adalah {jadwal_hari_ini}.")'''
   
f. Kode ini melakukan pengecekan pada variabel "jadwal_hari_ini". "Jika jadwal_hari_ini" tidak sama dengan (None), maka kode di dalam 
   baris (if) akan dijalankan.
      
  		'''else:'''
  
  		'''print(f"Kata kunci hari yang di input adalah  {input_hari}, berdasarkan kata kunci yang anda masukkan, tidak ada jadwal kuliah hari 
			ini.")'''
  
g. Kode ini akan dijaankan jika hasil ouput dari input-an pengguna menghasilkan nilai (none).

#2. Operator:

   (=) Operator penugasan untuk menyimpan nilai ke dalam variabe
   
   (.) Operator dot notation untuk mengakses method atau atribut dari suatu objek. Digunakan untuk mengakses method get() dan 
   capitalize() dari string dan dictionary.

#3. Flowchart

Berikut flowchart yang digunakan dalam kode tersebut:
    

![START (1)](https://github.com/Rifyal05/TugasAlgoritma1/assets/145568253/cb3dfd1b-a2c4-48e7-a5a2-7c2342000b48)
