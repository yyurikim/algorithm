import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

num_cnt = {}
left = 0
max_length = 0

for right in range(N):
    if lst[right] in num_cnt:
        num_cnt[lst[right]] += 1
    else:
        num_cnt[lst[right]] = 1

    while num_cnt[lst[right]] > K:
        num_cnt[lst[left]] -= 1
        if num_cnt[lst[left]] == 0:
            del num_cnt[lst[left]]
        left += 1

    max_length = max(max_length, right-left+1)

print(max_length)