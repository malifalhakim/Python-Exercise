word = input("Enter a string : ")

membership_word = ""

unique_char = True

for char in word:
    if char in membership_word:
        unique_char = False
        break

    membership_word += char

if unique_char :
    print("Yes")
else:
    print("No")