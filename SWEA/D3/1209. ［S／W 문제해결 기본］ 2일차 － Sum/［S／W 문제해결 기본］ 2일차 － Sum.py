for test_case in range(1, 11):
    tc_num = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    # i : rownum
    # j : columnnum

    sum_list = []

    # 열 우선 조회, 각각의 열 값들의 합 구하기
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += lst[i][j]
        sum_list.append(col_sum)

    # 행 우선 조회, 각각의 행 값들의 합 구하기
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += lst[i][j]
        sum_list.append(row_sum)

    dia_sum = 0
    # 대각선(오른쪽으로 진행) 합 구하기
    for k in range (100):
        dia_sum += lst[k][k]
        sum_list.append(dia_sum)

    dia_sum_2 = 0
    # 대각선(왼쪽으로 진행) 합 구하기
    for l in range (0,100):
        dia_sum_2 += lst[l][99-l]
        sum_list.append(dia_sum_2)

    print(f'#{test_case} {max(sum_list)}')