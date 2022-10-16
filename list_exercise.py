def count_neg(lst):
    lst_neg = []
    for elem in lst:
        count = 0
        for sub_elemen in elem :
            if sub_elemen < 0 :
                count += 1
        
        lst_neg.append(count)
    return lst_neg

print(count_neg([[0,-1],[-2,4],[-12,5],[4,-4]]))

""""
def is_sorted(lst):
    return lst == lst.sort()

"""

def is_sorted(lst):
    for i in range(len(lst)- 1):
        if not (lst[i] < lst[i + 1]):
            return False
    return True

print(is_sorted([1,7,8,3,4,5,6,7]))
