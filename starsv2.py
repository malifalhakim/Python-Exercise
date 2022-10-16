n = int(input("Enter a positive integer : "))

for i in range(1, n + 1):
    banyak_bintang = i
    banyak_spasi   = n - banyak_bintang

    print(" "*banyak_spasi + "*"*banyak_bintang)