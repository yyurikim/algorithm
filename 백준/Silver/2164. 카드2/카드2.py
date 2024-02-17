from collections import deque

N = int(input())

q = deque(list(range(1, N+1)))

while len(q) != 1:
    q.popleft()
    q.rotate(-1)

print(q[0])