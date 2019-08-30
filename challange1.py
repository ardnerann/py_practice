# challange 1
# x = 4
# y = 3
# z = 2

# w = ((x + y * z)/(x * y))**z
# print (w)

# challange 2
# import math
# angka = int(input('Silahkan masukkan angka berapa pun:'))
# print(math.sqrt(angka))

# challange 3
# import math

# tahun = 360
# bulan = 30

# hari = int(input('masukkan hari:'))
# hari_tahun = math.floor(hari/tahun)
# hari_sisa = hari-tahun
# print(hari_sisa)
# sisa_bulan = hari_sisa/bulan
# print(sisa_bulan)
# sisa_bulan1 = sisa_bulan - 4
# print(sisa_bulan1)
# sisa_hari1 = sisa_bulan1*30
# print(round(sisa_hari1))
# sisa_minggu = math.floor(sisa_hari1/7)
# print(sisa_minggu)
# print(str(hari) + ' hari sama dengan ' + str(hari_tahun) + ' tahun ' + str(round(sisa_bulan)) +' bulan ' + str(sisa_minggu) + ' minggu ' +str(round(sisa_hari1)) + ' hari.')



 

# challange 4
# UAB = 49
# usiaBudi = 490/14
# print('usia Budi adalah ' + str(int(usiaBudi)) + ' tahun')
# print('usia Andi adalah ' + str(int(UAB-usiaBudi)) + ' tahun')
# print('usia Andi dan Budi masing-masing dua tahun yang akan datang adalah: ' + str(int(UAB-usiaBudi+2)) + ' dan ' + str(int(usiaBudi +2)) + ' tahun.')

# # challange 5
# word = input('kata: ')
# countall = {i : word.count(i) for i in set(word)}
# print('Jumlah karakter yang terdapat pada kalimat ' + str(word)+ ' masing-masing adalah sebagai berikut: ' + str(countall))

# challange 6

DAB = int(input("Jarak antar kendaraan: "))
VA = int(input("Kecepatan kendaraan A: "))
VB = int(input("Kecepatan kendaraan B: "))

VAB = VA + VB
Time_minuteAB = (DAB/VAB) * 60

print(Time_minuteAB-60)


