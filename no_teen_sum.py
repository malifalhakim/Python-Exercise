def fix_teen(n):
    if n >= 13 and n <= 14 :
        value = 0
    elif n >= 17 and n <= 19 :
        value = 0
    else:
        value = n
    return value

def no_teen_sum (a,b,c):
    x = fix_teen(a)
    y = fix_teen(b)
    z = fix_teen(c)
    return x + y + z

print(no_teen_sum(2,13,1))
