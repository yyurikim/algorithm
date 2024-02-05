T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt_lst = [0]*101

    for i in range(len(lst)):
        cnt_lst[lst[i]] += 1

    mode_val = 0
    for j in range(len(cnt_lst)):
        if cnt_lst[j] >= cnt_lst[mode_val]:
            mode_val = j

    print(f'#{tc} {mode_val}')