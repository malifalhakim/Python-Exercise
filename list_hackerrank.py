N = int(input())
list = []

for i in range(N):
    command = input()
    if "insert" in command :
        command = command.split(" ")
        list.insert(int(command[1]),int(command[2]))
    elif "print" in command :
        print(list)
    elif "remove" in command :
        command = command.split(" ")
        list.remove(int(command[1]))
    elif "append" in command :
        command = command.split(" ")
        list.append(int(command[1]))
    elif "sort" in command :
        list.sort()
    elif "pop" in command :
        list.pop()
    elif "reverse" in command :
        list.reverse()