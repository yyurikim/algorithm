T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    time = [0] * 200

    for i in range(N):
        lst[i].sort()
        if lst[i][0] % 2 == 0:
            lst[i][0] -= 1
        if lst[i][1] % 2 == 0:
            lst[i][1] -= 1

        start_idx = lst[i][0]//2
        end_idx = lst[i][1]//2

        for t in range(start_idx, end_idx+1):
            time[t] += 1

    print(f'#{tc} {max(time)}')