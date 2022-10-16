file = open("transaksi.txt","r")

total_price = 0
for line in file :
    parts = line.split()
    total_price += int(parts[1]) * int(parts[2])

print(total_price)
file.close()