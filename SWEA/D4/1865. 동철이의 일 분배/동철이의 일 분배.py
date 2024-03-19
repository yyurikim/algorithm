def dfs(level):
    global cnt, max_cnt
    if level == N:
        if cnt > max_cnt:
            max_cnt = cnt
        return

    if cnt < max_cnt:
        return

    for i in range(N):
        if visited[i] or not lst[level][i]:
            continue
        visited[i] = 1
        cnt *= (lst[level][i])*0.01
        dfs(level+1)
        visited[i] = 0
        cnt /= (lst[level][i])*0.01

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    cnt = 1
    max_cnt = 0

    dfs(0)
    print(f'#{tc} {max_cnt*100:.6f}')