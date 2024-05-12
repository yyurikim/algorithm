import sys
input = sys.stdin.readline

N, K = map(int, input().split())

item_lst = [[0,0]]
d = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    item_lst.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        W = item_lst[i][0]
        V = item_lst[i][1]

        if j < W:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-W]+V)

print(d[N][K])