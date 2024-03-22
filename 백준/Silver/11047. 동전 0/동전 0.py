import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N-1, -1, -1):
    if lst[i] > K:
        continue

    else:
        if K == 0:
            break
        temp_num = K // lst[i]
        cnt += temp_num
        K -= temp_num * lst[i]

print(cnt)
