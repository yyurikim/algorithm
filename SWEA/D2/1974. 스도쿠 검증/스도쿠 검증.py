T = int(input())

for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로 탐색
    for i in range(9):
        cnt_lst = [0]*10
        ab_num = 0
        for j in range(9):
            cnt_lst[lst[i][j]] += 1
        if max(cnt_lst) >= 2:
            result = 0
            break

    # 세로 탐색
    for i in range(9):
        cnt_lst = [0]*10
        ab_num = 0
        for j in range(9):
            cnt_lst[lst[j][i]] += 1
        if max(cnt_lst) >= 2:
            result = 0
            break

    # 사각형 탐색
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            cnt_lst = [0] * 10
            for k in range(i, i+3):
                for l in range(j, j+3):
                    cnt_lst[lst[k][l]] += 1

        if max(cnt_lst) >= 2:
            result = 0
            break

    print(f'#{tc} {result}')