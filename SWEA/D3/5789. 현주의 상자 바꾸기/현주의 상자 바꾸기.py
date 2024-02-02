T = int(input())
for tc in range(1, T+1):
    lst_len, case_num = map(int, input().split())
    lst = [0] * (lst_len+1)
    for i in range(1, case_num+1):
        start_num, end_num = map(int, input().split())
        for j in range(start_num, end_num+1):
            lst[j] = i

    result = ' '.join(map(str, lst[1:]))
    print(f'#{tc} {result}')