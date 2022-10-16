def is_vowel(chr):
    return chr in 'aiueo'

def vowel_filter(word):
    """
    Mengembalikan huruf vokal dari word

    parameters:
        word(str):kata yang ingin diekstrak vokalnya

    return :
        sebuah string , urutan karakter vokal
    """
    vowel_str = ''
    for chr in word:
        if is_vowel(chr):
            vowel_str += chr
    return vowel_str

def scan_file(file_name):
    with open(file_name,'r') as file:
        for line in file:
            word = line.strip().lower()
            if vowel_filter(word) == 'aeiou':
                print(word)


if __name__ == '__main__':
    #testing unit
    assert vowel_filter('halo') == 'ao','program salah'
    assert vowel_filter('selamat') == 'eaa','program salah'
