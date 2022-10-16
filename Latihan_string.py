n = int(input())
str_kalimat = ""
while n > 0 :
    print("#"*n)
    n -= 1

n = int(input())

for i in range(1,n+1):
    if i % 2 == 1 :
        str_kalimat += "#"
    else :
        str_kalimat += "@"

print(str_kalimat)

