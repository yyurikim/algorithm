from collections import deque
import sys
input = sys.stdin.readline

row_idx = [0, 1, 0, -1]
col_idx = [1, 0, -1, 0]

def bfs(r, c):
    q = deque()
    q.append([r,c])
    visited[0] = 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            nr = row + row_idx[i]
            nc = col + col_idx[i]
            if (0<= nr < M and 0 <= nc < N):
                if [nr, nc] in jirung_info and not visited[jirung_info.index([nr, nc])]:
                    visited[jirung_info.index([nr, nc])] = 1
                    q.append([nr, nc])



T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    jirung_info = [list(map(int, input().split())) for _ in range(K)]
    visited = [0] * K
    cnt = 0

    for i in range(K):
        if not visited[i]:
            bfs(jirung_info[i][0], jirung_info[i][1])
            cnt += 1



    print(cnt)
