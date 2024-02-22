import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = []
max_val = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            hap = lst[i] + lst[j] + lst[k]
            if hap <= M and max_val < hap:
                max_val = hap

print(max_val)