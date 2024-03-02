import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
result = 0
nu = 0

for i in range(n):
    nu += lst[i]
    result += nu

print(result)