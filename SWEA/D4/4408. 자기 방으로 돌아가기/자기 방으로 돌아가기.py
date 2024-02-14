T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    room_lst = [0]*201

    cnt = 0

    for k in range(len(lst)):
        lst[k].sort()
        for j in range((lst[k][0]+1)//2, ((lst[k][1]+1)//2)+1):
            room_lst[j] += 1

    print(f'#{tc} {max(room_lst)}')