string_biner = input("String biner : ")

pangkat = 0
jumlah = 0

string_biner = string_biner[::-1]

for i in range(len(string_biner)):
    if i == len(string_biner) - 1:
        hasil = - (int(string_biner[i]) * ( 2 ** pangkat ))
        jumlah += hasil
        pangkat += 1
    else :
        hasil = int(string_biner[i]) * (2 ** pangkat)
        jumlah += hasil
        pangkat += 1

print(f"Signed Integer = {jumlah}") 

