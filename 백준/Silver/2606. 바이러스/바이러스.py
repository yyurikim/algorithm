import sys
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for nx in graph[start]:
        if visited[nx] == 0:
            dfs(nx)

N = int(input())

node = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(node):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(1)
print(sum(visited)-1)