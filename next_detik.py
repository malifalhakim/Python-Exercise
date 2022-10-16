'''SECURE PROGRAMMING'''

jam   = int(input("Jam   : "))
menit = int(input("Menit : "))
detik = int(input("Detik : "))

if 0 <= jam <= 23 and 0 <= menit <= 59 and 0 <= detik <= 59:

    DETIK_PER_JAM = 3600
    DETIK_PER_MENIT = 60

    total_detik = jam * DETIK_PER_JAM + menit * DETIK_PER_MENIT + detik

    next_detik = total_detik + 1

    jam = ( next_detik // DETIK_PER_JAM ) % 24

    menit = ( next_detik % DETIK_PER_JAM ) // DETIK_PER_MENIT

    detik = ( next_detik % DETIK_PER_MENIT)

    print(f"Waktu setelah 1 detik = {jam} - {menit} - {detik}")

else :
    print("Input Error")