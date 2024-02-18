from collections import deque

N, K = map(int, input().split())

q = deque(list(range(1, N+1)))

result = []

while q:
    for i in range(K-1):
        q.rotate(-1)
    result.append(q.popleft())

print('<', end='')

for num in result[:-1]:
    print(f'{num},', end=' ')

print(result[-1], end='')

print('>', end='')