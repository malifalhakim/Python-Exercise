def modify_lst(i,lst):
    new_element = lst[i] + lst[-1]
    lst[-1] = new_element
    lst.remove(lst[i])
    return lst

def check_larger(i,lst):
    for num in lst[i:]:
        if lst[i] > num:
            return True
    return False

number_of_cases = int(input())

for cases in range(number_of_cases):
    array_size = int(input())
    array_lst = input().split()
    array_lst = [int(num) for num in array_lst]
    i = 0
    count = 0
    while i < len(array_lst):
        if check_larger(i,array_lst):
            array_lst = modify_lst(i,array_lst)
            count += 1
        else :
            i += 1
    

    print(count)


