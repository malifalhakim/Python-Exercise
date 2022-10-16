def decimal_to(decimal,basis):
    hasil_bagi = decimal // basis
    sisa_bagi = decimal % basis
    hasil_konversi = str(sisa_bagi)

    while hasil_bagi > 0 :
        hasil_bagi, sisa_bagi = hasil_bagi // basis , hasil_bagi % basis
        hasil_konversi += str(sisa_bagi)

    return hasil_konversi[::-1]

if __name__ == '__main__':
    print("Selamat datang di Bunker Hacker!")
    status = False
    while not status :
        try:
            banyak_konversi = int(input("Masukkan berapa kali konversi ingin dilakukan : "))
            basis_konversi = input("Sebutkan semua tujuan basis yang ingin dikonversi (pisah dengan spasi): ").split()
            basis_konversi = [int(i) for i in basis_konversi]
            for i in range(banyak_konversi):
                angka_decimal = int(input(f"\nMasukkan angka ke-{i + 1} yang ingin dikonversi : "))
                for j in range(len(basis_konversi)):
                    print(f"Hasil Konversi desimal ke basis {basis_konversi[j]} : {decimal_to(angka_decimal,basis_konversi[j])}")
            status = True
        except ValueError:
            print("Input tidak valid")

    print("\nTerima kasih telah menggunakan Bunker Hacker")