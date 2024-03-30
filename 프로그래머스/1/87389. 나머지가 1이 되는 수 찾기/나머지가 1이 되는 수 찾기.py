def solution(n):
    temp = n-1
    num = 2
    while temp % num != 0:
        num += 1
        
    return num