def min(a,b):
    if a > b :
        return b
    else :
        return a


N = int(input())

for x in range(N):
    lst_size_K= input().split()
    K = int(lst_size_K[1])
    lst = input().split()
    lst = [int(num) for num in lst]
    lst.sort()
    while len(lst) > 1:
        if len(lst) > K :
            minimum = min(lst[0],lst[1])
            lst[1] = minimum
            lst.remove(lst[0])
        elif len(lst) == K :
            maximum = max(lst)
            lst = [maximum]
    if lst == [1]:
        print('YES')
    else :
        print('NO')
    


