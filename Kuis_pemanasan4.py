string_biner = input("String biner : ")
string_biner_check = False

while not string_biner_check:
    for char in string_biner :
        if char != '1' and char != '0' :
            print("Input harus dalam biner")
            string_biner = input("String biner : ")
        else :
            string_biner_check = True
    
#Mengubah most significant bit ke kanan

string_biner = string_biner[::-1]

pangkat = 0
jumlah  = 0

for i in string_biner:
    hasil = int(i) * (2 ** pangkat )
    jumlah += hasil

    pangkat += 1

print(f"Unsigned integer : {jumlah}")
