from collections import deque

def solution(maps):
    
    x_lst = [0, -1, 1, 0]
    y_lst = [1, 0, 0, -1]
    
    q = deque([[0,0]])
    
    x_idx = 0
    y_idx = 0
    
    n = len(maps)
    m = len(maps[0])
    
    cnt = 0
    
    while q:
        temp = q.popleft()        
        
        for i in range(4):
            x_idx = temp[0] + x_lst[i]
            y_idx = temp[1] + y_lst[i]
            if 0 <= x_idx < n and 0 <= y_idx < m:
                if maps[x_idx][y_idx] == 1:
                    q.append([x_idx, y_idx])
                    maps[x_idx][y_idx] = maps[temp[0]][temp[1]] + 1
        
    
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    
    return answer