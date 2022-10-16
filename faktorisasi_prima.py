def faktorisasi_prima(num):
    pembagi = 2
    hasil_bagi = num
    faktor_prima = ''
    while pembagi < hasil_bagi :
        pangkat = 0
        while hasil_bagi % pembagi == 0:
            if not( str(pembagi) in faktor_prima):
                faktor_prima += str(pembagi)
            else:
                pangkat += 1
        print(f"{pembagi}^{pangkat}",end='')
        pembagi += 1

faktorisasi_prima(100)




