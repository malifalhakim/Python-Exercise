banyak_pengecekan = int(input())

for cek in range(banyak_pengecekan) :
    angka_cek = input().split()
    a = int(angka_cek[0])
    b = int(angka_cek[1])
    c = int(angka_cek[2])
    if a +b == c or a + c == b or b + c == a:
        print('YES')
    else:
        print('NO')