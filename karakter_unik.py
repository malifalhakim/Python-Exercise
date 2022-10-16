
def unique_words(file_name):
    with open(file_name,'r') as file:
        list_of_unique_char = []
        for line in file:
            words = line.split()
            for word in words:
                if not (word in list_of_unique_char):
                    list_of_unique_char.append(word)
    return list_of_unique_char

list_of_unique_char = unique_words('input1.txt')
for unique_word in list_of_unique_char:
    print(unique_word)