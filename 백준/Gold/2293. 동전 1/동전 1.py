import sys
input = sys.stdin.readline

lst = []
n, k = map(int, input().split())
for _ in range(n):
    lst.append(int(input()))
lst.sort()

ways_lst = [0] * (k+1)

ways_lst[0] = 1

for i in lst:
    for j in range(i, k+1):
        ways_lst[j] = ways_lst[j] + ways_lst[j-i]

print(ways_lst[k])