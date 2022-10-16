'''Naik Gaji'''
GAJI_AWAL = int(input("Masukkan Gaji Awal : "))

PERSEN_NAIK = 0.02

gaji_sekarang = GAJI_AWAL

tahun = 0

GAJI_DUA_KALI_LIPAT = GAJI_AWAL * 2

while gaji_sekarang < GAJI_DUA_KALI_LIPAT :
    gaji_sekarang = (1 + PERSEN_NAIK ) * gaji_sekarang
    tahun += 1

print(f"Tahun yang dibutuhkan agar gaji jadi dua kali lipat = {tahun}")

