check = False
while not check:
    try:
        nama_file = input("Nama File : ")
        file = open(nama_file,"r")

        vowel = 'aiueo'
        count = 0

        for line in file :
            set_of_word = line.split()

            for word in set_of_word:
                if not( word[-1] in vowel) :
                    count += 1

        print(f"Ada {count} yang diakhiri huruf konsonan")
        file.close()
        
        check = True
    except FileNotFoundError:
        print("File tidak ditemukan!")