import math

def solution(brown, yellow):
    answer = []
    
    lst = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i ==0:
            lst.append([i, yellow//i])
    
    
    for case in lst:
        if case[0]*case[1] + 2*case[0] + 2*case[1] + 4 == brown+yellow:
            answer.append(case[1]+2)
            answer.append(case[0]+2)
    
    return answer