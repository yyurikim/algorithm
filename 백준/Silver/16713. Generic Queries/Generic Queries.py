import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

lst = [0] + list(map(int, input().split()))


# 먼저 리스트의 xor 누적 결과를 계산
for i in range(1, N+1):
    lst[i] = lst[i-1] ^ lst[i]


# 각 쿼리의 xor 결과를 반복해서 계산
result = 0
for _ in range(Q):
    s, e = map(int, input().split())
    result = result ^ (lst[e] ^ lst[s-1])

print(result)