import random

nilai_n = int(input("Nilai N : "))
nilai_k = int(input("Nilai K : "))

print("\n")

banyak_k = 0

for i in range(1,nilai_n + 1):
    dadu_didapat = random.randint(1,6)
    print("nilai dadu loop",i,"=",dadu_didapat)
    if dadu_didapat == nilai_k :
        banyak_k += 1

print("banyak kemunculan angka",nilai_k,"=",banyak_k)
