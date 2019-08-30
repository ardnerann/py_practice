# angka = 0
# while(angka <= 100):
#     print(angka)
#     angka += 2

# listItem = list(range(1,100,5))
# print(listItem)

# for item in range(1,100,5):
#     print(item)

# absen = 'Nomor urut anda: '
# for item in range(1,11):
#     print(absen + str(item))

# absen = 'Nomor urut anda: '
# for item in range(0,22,2):
#     print(absen + str(item))

# Loop drawing

z=''

# for item in range(0,5):
#     z += ' * '
# print(z)

# for item in range(0,5):
#     z += ' * \n'
# print(z)

# for item in range(0,5):
#     for item1 in range(0,5):
#         z += ' * '
#     z += '\n'
# print(z)

for item in range(0,5): # versi sendiri
    z += ' * '
    print(z)

z='' # versi guru
for item in range(5):
    for item1 in range(0, item+1):
        z += ' * '
    z += '\n'
print(z)