jadwal = {"Senin" : "Matematika diskrit, Jam = 08:00-09:20, Ruangan= D4.3" " dan " "Bahasa inggris, Jam = 09:20-10:40, Ruangan = D4.2",
          "Selasa": "Analisis dan Desain Perangkat Lunak, Jam = 08:40-10:00, Ruangan : D4.4 Dan Kewaganegaraan, Jam = 12:00-13:20, Ruangan = D4.3",
          "Kamis" : "Algoritma dan struktur data 2, Jam 12:00-14:00, Ruangan = D4.2 Dan E-commerce, Jam = 14:00-15=20, Ruangan = D4.3",
          "Jumat" : "Aljabar Linear, Jam 08:00-09:20, Ruangan = D4.2 , Pengantar Rekayasa Perangkat Lunak, Jam = 09.20-10.40, Ruangan = D4.6, Dan Interaksi manusia dan komputer, Jam = 13:00-14:20, Ruangan = D4.4"}

input_hari =str(input("Masukan Kata kunci dalam bentuk nama hari (Senin/Selasa dst...): "))

input_hari = input_hari.capitalize()
jadwal_hari_ini = jadwal.get(input_hari)

if jadwal_hari_ini:
      print(f"Kata kunci hari yang di input adalah {input_hari} , Berdasarkan kata kunci yang di input, jadwal kuliah untuk hari ini adalah {jadwal_hari_ini}.")
else:
      print(f"Kata kunci hari yang di input adalah  {input_hari}, berdasarkan kata kunci yang anda masukkan, tidak ada jadwal kuliah hari ini.")
