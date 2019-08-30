filter = str(input('Masukkan kata yang ingin anda cari: '))
import re

kata = ['Merdeka', 'Hello', 'Hellos', 'Kari Ayam', 'Tidur', ]


regex = re.compile(''.join(filter), re.IGNORECASE)
kata_filter = [word for word in kata if regex.search(word)]
print(kata_filter)

