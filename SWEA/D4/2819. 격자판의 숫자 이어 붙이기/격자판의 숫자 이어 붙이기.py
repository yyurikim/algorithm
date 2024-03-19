def dfs(cnt, row, col,num):
    row_idx = [0, 1, 0, -1]
    col_idx = [1, 0, -1, 0]
    num += lst[row][col]

    if cnt == 6:
        num_lst.append(num)
        return

    for i in range(4):
        nr = row + row_idx[i]
        nc = col + col_idx[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(cnt+1, nr, nc, num)

T = int(input())

for tc in range(1, T+1):
    lst = [list(map(str, input().split())) for _ in range(4)]
    num_lst = []

    for i in range(4):
        for j in range(4):
            dfs(0, i, j, '')

    num_lst = set(num_lst)
    print(f'#{tc} {len(num_lst)}')