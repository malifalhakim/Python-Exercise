import random

#Memasukkan input jumlah dadu
valid = False

while not valid :
    total_sum = int(input("Total Sum = "))
    if total_sum > 0 :
        valid = True
    else :
        print("Tolong masukkan input dengan benar")

#Menset nilai awal dari banyak lemparan dan total masing masing dadu
banyak_lemparan_a = 0
total_a = 0

banyak_lemparan_b = 0
total_b = 0

print("\n")

#melakukan pelemparan dadu dan penghitungan total

while (total_a < total_sum) and (total_b < total_sum) :
    dadu_a = random.randint(1,6)
    total_a += dadu_a 

    dadu_b = random.randint(1,6)
    total_b += dadu_b

    print(f"dadu A : {dadu_a} total A : {total_a} --- dadu B : {dadu_b} total B : {total_b}")

#Menentukan siapa yang menang

if total_a >= total_sum and total_b < total_sum :
    print("A Menang")
elif total_a < total_sum and total_b >= total_sum:
    print("B Menang")
else :
    print("A dan B Menang")


