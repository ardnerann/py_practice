# soal 1

# angka = (float(input('masukkan angka: ')))
# angka1 = angka % 2
# if angka1 > 0 :
#     print( 'angka ' + str(int(angka)) + ' adalah angka ganjil.')
# else :
#     print('angka ' + str(int(angka)) + ' adalah angka genap.')

# soal 2

berat_badan = float(input('Masukkan berat badan anda (dalam kg) :'))
tinggi = float(input('Masukkan tinggi badan anda (dalam cm): '))/100
BB = berat_badan/((tinggi)**2)
print('Berat badan anda ' + str(berat_badan) + 'kg')
print('Tinggi badan anda ' + str(tinggi) + 'm')



if BB < 18.5:
    print('IMT ' + str(BB) + ' berat badan anda kurang')
elif BB >= 18.5 and BB <= 24.9:
    print('IMT ' + str(BB) + ' berat badan anda ideal')
elif BB >= 25.0 and BB <= 29.9:
    print('IMT ' + str(BB) + ' berat badan anda berlebih')
elif BB >= 30.0 and BB <= 39.9:
    print('IMT ' + str(BB) + ' berat badan anda sangat berlebih')
else :
    print('IMT ' + str(BB) + ' anda mengalami obesitas')




