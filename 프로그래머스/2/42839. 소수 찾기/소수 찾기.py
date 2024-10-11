from itertools import permutations
import math

def solution(numbers):
    answer = 0
    lst = []
    numbers_lst = list(numbers)
    for i in range(1,len(numbers_lst)+1):
        lst = lst + list(set(permutations(numbers_lst,i)))
        
    real_nums = []
    for num in lst:
        real_nums.append(int(''.join(num)))
    
    real_nums = list(set(real_nums))
    
    for num in real_nums:
        flag = True
        if num == 0 or num == 1:
            flag = False
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    flag = False
                    break
        if flag == True:
            answer +=1
    
    return answer