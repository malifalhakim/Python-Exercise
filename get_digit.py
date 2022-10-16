def get_digit(number,position):
    '''return digit in position in number counting from right'''
    number = str(number)
    number = number[::-1]

    return int(number[position])

def check_konsonan (word):
    count = 0
    vowel = 'AIUEOaiueo'
    for chr in word:
        if chr not in vowel :
            count += 1

    return count




print(get_digit(31421,0))