import sys
import statistics

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
max_score = max(lst)

for i in range(N):
    lst[i] = lst[i]/max_score*100


print(statistics.mean(lst))