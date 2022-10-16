word = input("Enter a word : ")

abcedarian_status = True

for i in range(len(word) - 1):
    if ord(word[i]) > ord(word[i+1]):
        abcedarian_status = False

if abcedarian_status :
    print(word,"is abecedarian")
else:
    print(word,"is not abecedarian")