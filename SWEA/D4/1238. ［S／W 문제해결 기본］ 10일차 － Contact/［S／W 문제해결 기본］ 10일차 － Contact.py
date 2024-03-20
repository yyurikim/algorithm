from collections import deque
 
def bfs(s):
    q = deque()
    visited = [0] * 101
    q.append(s)
    visited[s] = 1
    while q:
        pt = q.popleft()
        for j in adjl[pt]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1 + visited[pt]
    max_num = 0
    max_val = 0
    for k in range(101):
        if visited[k] >= max_val:
            max_val = visited[k]
            max_num = k
 
    return max_num
 
for tc in range(1, 11):
    L, S = map(int, input().split())
    t = list(map(int, input().split()))
 
    adjl = [[] for _ in range(101)]
    for i in range(0, L, 2):
        n1, n2 = t[i], t[i+1]
        adjl[n1].append(n2)
 
    print(f'#{tc} {bfs(S)}')