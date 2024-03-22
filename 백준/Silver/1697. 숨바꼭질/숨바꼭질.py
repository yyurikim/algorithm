from collections import deque
import sys

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        temp = [now-1, now+1, now*2]
        for t in temp:
            if 0 <= t <= 100000 and not visited[t]:
                visited[t] = visited[now] + 1
                q.append(t)


input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001

bfs(N)
print(visited[K]-visited[N])