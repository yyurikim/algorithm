from collections import deque
import sys
input = sys.stdin.readline


row_idx = [0, 1, 0, -1]
col_idx = [1, 0, -1, 0]


def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        nr, nc = q.popleft()
        for i in range(4):
            pr = nr + row_idx[i]
            pc = nc + col_idx[i]
            if (0 <= pr < N and 0<= pc < M) and lst[pr][pc] == 1 and not visited[pr][pc]:
                q.append([pr, pc])
                visited[pr][pc] = visited[nr][nc] + 1

N, M = map(int, input().split())
lst = [list(map(int, input().rstrip())) for _ in range(N)]


visited = [[0]*M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])