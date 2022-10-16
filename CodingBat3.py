def round10(num):
    sisa_angka = num % 10
    if sisa_angka >= 5:
      num = (num // 10 ) * 10
      num += 10
    else:
      num = (num // 10 ) * 10
    return num

def round_sum (a , b ,c):
    a = round10(a)
    b = round10(b)
    c = round10(c)
    hasil = a + b + c
    return hasil

print(round_sum(14,12,16))