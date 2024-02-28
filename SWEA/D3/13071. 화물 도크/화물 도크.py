T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst.sort(key = lambda x:x[1])
    start_time = lst[0][0]
    end_time = lst[0][1]
    cnt = 1

    for i in range(1, len(lst)):
        if lst[i][0] >= end_time:
            start_time = lst[i][0]
            end_time = lst[i][1]
            cnt +=1

    print(f'#{tc} {cnt}')