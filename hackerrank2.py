if __name__ == '__main__':
    all_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data = [name,score]
        all_data.append(student_data)
        
sorted_data = sorted(all_data,key = lambda x : x[1])
print(sorted_data)

first_lowest = []

for i in range(len(sorted_data)):
    if sorted_data[0][1] == sorted_data[i][1]:
        first_lowest.append(sorted_data[i])
    else:
        second_lowest = sorted_data[i]
        break
    
second_lowest_list = []
for data in sorted_data:
    if second_lowest[1] == data[1]:
        second_lowest_list.append(data)
        
second_lowest_list.sort()

for name in second_lowest_list :
    print(name[0])
    