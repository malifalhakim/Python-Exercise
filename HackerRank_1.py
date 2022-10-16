


def avg(list_num):
    total = 0
    for number in list_num :
        total += number
    avarage = total / len(list_num)
    return avarage

num_input = input().split()
list_input = []
for num in num_input:
    num = int(num)
    list_input.append(num)

x = avg(list_input)
print(x)