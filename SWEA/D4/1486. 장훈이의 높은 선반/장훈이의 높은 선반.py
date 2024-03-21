def dfs(height, level):
    global min_height
    if level == N:
        if height >= B:
            min_height = min(height, min_height)
        return

    dfs(height + lst[level], level + 1)
    dfs(height, level + 1)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    min_height = float('inf')


    dfs(0, 0)

    print(f'#{tc} {min_height-B}')