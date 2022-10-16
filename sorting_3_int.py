'''Sorting 3 Integers'''

a = int(input('Angka 1 : '))
b = int(input('Angka 2 : '))
c = int(input('Angka 3 : '))

##1.Pakai Nested List

##2.Bubble Sort
if a > b:
    a , b = b , a

if b > c :
    b , c = c , b

if a > b :
    a , b = b , a

print(f"{a},{b},{c}")
