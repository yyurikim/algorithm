from collections import deque

row_idx = [0, 1, 0, -1]
col_idx = [1, 0, -1, 0]

def bfs(lst):
    q = deque()
    q.append([1, 1])
    while q:
        idx = q.popleft()
        lst[idx[0]][idx[1]] = 1  # 방문표시

        for i in range(4):
            row = idx[0] + row_idx[i]
            col = idx[1] + col_idx[i]

            if 1<= row <=15 and 1<= col <= 15 and lst[row][col] == 0:
                q.append([row, col])
                lst[row][col] = 1  # 중복방문을 막기위해

            elif lst[row][col] == 3:
                return 1
                break

for tc in range(1,11):
    T = int(input())
    maze_lst = [list(map(int, input())) for _ in range(16)]

    if bfs(maze_lst):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')