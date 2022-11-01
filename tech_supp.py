from itertools import count


number_of_cases = int(input())

for cases in range(number_of_cases):
    number_interaction = int(input())
    input_interact = input()

    for i in range(len(input_interact)) :
        if input_interact[i] == 'Q':
            count_Q = 0
            count_A = 0
            for j in range(i,len(input_interact)):
                if input_interact[j] == 'Q':
                    count_Q += 1
                else :
                    break
            for k in range(i,len(input_interact)):
                if input_interact[k] == 'A':
                    count_A += 1
                else :
                    break
            if count_A >
        else :
            pass
