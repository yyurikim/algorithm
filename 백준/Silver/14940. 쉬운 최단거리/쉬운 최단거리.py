import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(N)]
idx = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 목표지점까지의 거리를 출력할 리스트, 기본 값을 -1(도달할 수 없는 위치일 때의 값)로 지정
result_lst = [[-1]*M for _ in range(N)]

# 목표 지점의 위치 탐색
for i in range(N):
    for j in range(M):
        if map_lst[i][j] == 2:
            start_row, start_col = i, j # 목표 지점의 위치는 start_row, start_col에 저장
        elif map_lst[i][j] == 0:
            result_lst[i][j] = 0 # 갈 수 없는 땅은 값을 0으로 변경

# 목표 지점 (bfs 시작 지점) queue에 추가
q = deque([[start_row, start_col]])
# 목표 지점 (bfs 시작 지점) 값 0으로 변경
result_lst[start_row][start_col]=0

# bfs로 갈 수 있는 땅 모두 탐색
while q:
    row, col = q.popleft()

    for r, c in idx:
        n_row = row + r
        n_col = col + c

        # 좌표가 범위 안이고, 아직 방문하지 않았으며 도달할 수 있는 위치일때만 탐색
        if 0 <= n_row < N and 0 <= n_col < M and result_lst[n_row][n_col] == -1 and map_lst[n_row][n_col]==1:
            q.append([n_row, n_col])
            result_lst[n_row][n_col] = result_lst[row][col]+1


for l in result_lst:
    print(' '.join(list(map(str, l))))