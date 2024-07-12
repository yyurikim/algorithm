import sys

input = sys.stdin.readline

T = int(input())

checkpoints = [list(map(int, input().split())) for _ in range(T)]

distances = []

for i in range(T-1):
    distances.append(abs(checkpoints[i][0] - checkpoints[i+1][0]) + abs(checkpoints[i][1] - checkpoints[i+1][1]))

total_distance = sum(distances)


min_val = float('inf')


for j in range(1, T-1):
    sum_val = total_distance - distances[j-1] - distances[j] + abs(checkpoints[j-1][0] - checkpoints[j+1][0]) + abs(checkpoints[j-1][1] - checkpoints[j+1][1])
    if sum_val < min_val:
        min_val = sum_val


print(min_val)