T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle += list(map(list,zip(*puzzle)))

    result = 0
    cnt = 0

    for i in range(2*N):
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
                if j == N-1:
                    if cnt == K:
                        result += 1
                        cnt = 0
                    else:
                        cnt = 0
            elif puzzle[i][j] == 0:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0

    print(f'#{tc} {result}')