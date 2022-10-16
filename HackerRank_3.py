x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_x = [i for i in range(x + 1)]
list_y = [i for i in range(y + 1)]
list_z = [i for i in range(z + 1)]

list_array = []
list_child = []
for x in list_x:
    
    for y in list_y:
        
        for z in list_z:
            list_child.append(x)
            list_child.append(y)
            list_child.append(z)
            list_array.append(list_child)
            list_child = []

print(list_array)

list_array = [item for item in list_array if item[0]+item[1]+item[2]!=n]

print(list_array)