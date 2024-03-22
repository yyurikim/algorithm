from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque()
    q.extend(lst[start])

    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = 1
            q.extend(lst[now])

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    for _ in range(M):
        per1, per2 = map(int, input().split())
        lst[per1].append(per2)
        lst[per2].append(per1)
    visited = [0] * (N+1)
    group_cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            group_cnt += 1

    print(f'#{tc} {group_cnt}')