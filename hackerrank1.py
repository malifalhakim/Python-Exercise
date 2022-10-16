n = int(input())
arr = map(int, input().split())
 
score_list = []    
for score in arr :
    score_list.append(score)
    
score_list.sort()
print(score_list[-2])