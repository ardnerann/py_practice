#!/usr/bin/env python
# coding: utf-8

# Soal no 1

# In[21]:


n = 2
  
angka = [int(i) for i in input('Masukkan bilangan: ').split()] 
angka = (angka[len(angka) - n:len(angka)]  
                 + angka[0:len(angka) - n]) 
print(angka) 


# Soal no 2

# In[2]:


import math
rad = int(input('Masukkan nilai radius: '))
A = math.pi * (rad**2) 
print('Jadi, luas lingkaran adalah: ' + str(A) + ' satuan.')


# Soal no 3

# In[20]:


a = int(input('Masukkan angka pertama: '))
b = int(input('Masukkan angka kedua: '))
total = str(a) + str(b)
print(total)


# Soal no 4

# In[4]:


phrase = str(input('Masukkan kalimat: '))
removed_phrase = str(input('Pilih karakter yang akan dihilangkan: '))
phrase.translate({ord(removed_phrase): None})


# In[13]:


words = str(input('Masukkan dua kata: '))
upside_words = words[0:5]
print(upside_words)


# In[25]:


word1 = str(input('Masukkan kata pertama: '))
word2 = str(input('Masukkan kata kedua: '))

swap = word2 + ' ' + word1
print(swap)


# In[ ]:




