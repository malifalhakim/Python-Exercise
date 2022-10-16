import math


banyak_baris = int(input("Banyak Baris : "))
banyak_kolom = int(input("Banyak Kolom : "))

banyak_entry_per_halaman = banyak_baris * banyak_kolom

entry_dicari = int(input("Entry : "))

#Letak Kolom

if entry_dicari % banyak_kolom == 0:
    letak_kolom = banyak_kolom
else:
    letak_kolom = entry_dicari % banyak_kolom

#Letak Baris

letak_baris = math.ceil(entry_dicari / banyak_kolom)
if letak_baris > banyak_kolom:
    letak_baris = letak_baris % banyak_kolom

#Letak Halaman

letak_halaman = math.ceil(entry_dicari/banyak_entry_per_halaman)

print("Entry ke",entry_dicari,"terletak pada :")
print("Baris ->",letak_baris)
print("Kolom ->",letak_kolom)
print("Halaman ->",letak_halaman)