lst = [list(map(int, input().split())) for _ in range(9)]

max_val = 0
max_row, max_col = 0, 0
for i in range(9):
    for j in range(9):
        if lst[i][j] > max_val:
            max_val = lst[i][j]
            max_row, max_col = i, j

print(max_val)
print(max_row+1, max_col+1)