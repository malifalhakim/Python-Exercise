word_1 = input("Sentence 1 : ").lower()
word_2 = input("Sentence 2 : ").lower()

word_1 = word_1.split(" ")

print("\nIrisan : ")
for word in word_1 :
    if word in word_2 :
        print(word)
