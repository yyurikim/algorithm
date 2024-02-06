T = int(input())

for tc in range(1, T+1):
    lst_len = int(input())

    tri_lst = [[0]*(lst_len+1) for _ in range(lst_len)]

    tri_lst[0][1] = 1

    for i in range(1, lst_len):
        for j in range(1, i+2):
            tri_lst[i][j] = tri_lst[i-1][j-1] + tri_lst[i-1][j]

    print(f'#{tc}')
    for k in range(lst_len):
        result = ' '.join(map(str, tri_lst[k][1:k+2]))
        print(result)