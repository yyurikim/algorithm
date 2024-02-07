row, col = map(int, input().split())

lst_1 = [list(map(int, input().split())) for _ in range(row)]
lst_2 = [list(map(int, input().split())) for _ in range(row)]
result = [[0] * col for _ in range(row)]

for r in range(row):
    for c in range(col):
        result[r][c] = lst_1[r][c] + lst_2[r][c]


for j in range(len(result)):
    print(*result[j])
