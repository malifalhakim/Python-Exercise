def shift_left(lst):
    return lst[1:] + [lst[0]]
def shift_let_n(n,lst):
    for i in range(n):
        lst = shift_left(lst)
    return lst

print(shift_left([231,1241,1231]))
print(shift_let_n(2,[1,2,3,4]))