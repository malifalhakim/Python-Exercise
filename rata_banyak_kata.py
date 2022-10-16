file = open("puisi.txt","r")

total_word = 0
total_line = 0

for line in file :
    total_word += len(line.split())
    total_line += 1

rata_rata = total_word / total_line
print(f"Rata-rata banyak kata per baris adalah {rata_rata}")
