'''Double Char'''

def double_char(str):
    new_str = ''
    for i in str :
        huruf = i * 2
        new_str += huruf
    return new_str

print(double_char("Oha"))
