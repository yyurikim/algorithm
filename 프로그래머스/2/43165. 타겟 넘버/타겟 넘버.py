answer = 0

def solution(numbers, target):

    
    def dfs(idx, sum_val):
        global answer
        if idx == len(numbers):
            if sum_val == target:
                answer += 1
            return
        
        dfs(idx+1, sum_val + numbers[idx])
        dfs(idx+1, sum_val - numbers[idx])
        
    
    dfs(0,0)
    
    return answer