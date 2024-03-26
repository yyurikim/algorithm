#                     elif j % 2 == 1:
#                         if board[i][j] == 'W':
#                             result2 += 1
#                         elif board[i][j] == 'B':
#                             result1 += 1
#
#         temp = min(result1, result2)
#         if temp < min_result:
#             min_result = temp
#
# print(min_result)

from collections import deque

row_idx = [0, 1, 0, -1]
col_idx = [1, 0, -1, 0]

def bfs(r, c):
    global cnt
    q = deque()
    q.append([r, c])
    MAP[r][c] = 0
    cnt = 1

    while q:
        row, col = q.popleft()

        for i in range(4):
            nr = row + row_idx[i]
            nc = col + col_idx[i]
            if 0 <= nr < N and 0 <= nc < N and MAP[nr][nc] == 1:
                q.append([nr, nc])
                MAP[nr][nc] = 0
                cnt += 1


N = int(input())

MAP = [list(map(int, input().strip())) for _ in range(N)]

cnt_lst = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            cnt = 0
            bfs(i, j)
            cnt_lst.append(cnt)


print(len(cnt_lst))
cnt_lst.sort()
for num in cnt_lst:
    print(num)