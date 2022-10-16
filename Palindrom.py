word = input("Masukkan kata : ")

kiri = 0
kanan = len(word) - 1

while kiri < kanan :
    if word[kiri] == word [kanan]:
        status_palindrom = True
    else :
        status_palindrom = False

    kiri += 1
    kanan -= 1

if status_palindrom :
    print("Palindrom")
else :
    print("Bukan Palindrom")