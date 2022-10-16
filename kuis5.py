nama_file = input("Nama File : ")

try :
    file = open(nama_file,"r")

    for line in file :
        set_of_word = line.split()
        reverse_set_of_word = set_of_word[::-1]
        sentence = ''
        for word in reverse_set_of_word :
            sentence += word + ' '
        
        print(sentence)
        
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan !")