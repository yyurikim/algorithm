import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

min_result = float('inf')

for n in range(N-8+1):
    for m in range(M-8+1):
        # result1 : 시작이 w
        result1 = 0
        # result2 : 시작이 b
        result2 = 0
        for i in range(n, n+8):
            for j in range(m, m+8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if board[i][j] == 'W':
                            result2 += 1
                        elif board[i][j] == 'B':
                            result1 += 1
                    elif j % 2 == 1:
                        if board[i][j] == 'W':
                            result1 += 1
                        elif board[i][j] == 'B':
                            result2 += 1

                elif i % 2 == 1:
                    if j % 2 == 0:
                        if board[i][j] == 'W':
                            result1 += 1
                        elif board[i][j] == 'B':
                            result2 += 1
                    elif j % 2 == 1:
                        if board[i][j] == 'W':
                            result2 += 1
                        elif board[i][j] == 'B':
                            result1 += 1

        temp = min(result1, result2)
        if temp < min_result:
            min_result = temp

print(min_result)