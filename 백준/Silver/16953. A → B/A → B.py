import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    visited = {}
    q = deque()
    q.append(A)
    visited[A] = 1

    while q:
        num = q.popleft()
        if num == B:
            return visited[B]

        if num > B:
            continue

        temp = [num * 2, int(str(num) + '1')]

        for t in temp:
            if t not in visited:
                visited[t] = visited[num] + 1
                q.append(t)
            if visited[t] < visited[num] + 1:
                visited[t] = visited[num] + 1
                q.append(t)

    return -1

A, B = map(int, input().split())

print(bfs(A))