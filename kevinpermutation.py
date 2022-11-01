
N = int(input())

for cases in range(N):
    num = int(input())
    lst = [i for i in range(1,num + 1)]
    if len(lst) > 3:
        if len(lst) % 2 == 0:
            lst1 = lst[ : int(len(lst)/2)]
            lst1 = lst1 [::-1]
            lst2 = lst[int(len(lst)/2)  :]
            lst2 = lst2[::-1]
        else:
            lst1 = lst[ : int(len(lst)/2) + 1]
            lst1 = lst1 [::-1]
            lst2 = lst[ int(len(lst)/2) + 1 : ]
            lst2 = lst2[::-1]
            lst2.append(0)

        new_lst = []
        for i in range(len(lst1)):
            new_lst.append(lst1[i])
            new_lst.append(lst2[i])
        if len(lst) % 2 == 1:
            new_lst.remove(new_lst[-1])
        for num in new_lst:
            print(num,end=' ')
    else :
        for num in lst:
            print(num , end = ' ')
    print()