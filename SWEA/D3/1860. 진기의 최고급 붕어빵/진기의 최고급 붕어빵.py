T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cust_info = list(map(int, input().split()))
    result = 'Possible'
    b_lst = [0] * 11112
    b_idx = 0

    for i in range(0, 11112, M):
        b_lst[i] = K

    b_lst[0] = 0

    for j in cust_info:
        if b_lst[j] != 0:
            b_lst[j] -= 1
        else:
            if sum(b_lst[:j+1]) <= 0:
                result = 'Impossible'
                break
            else:
                for k in range(j, 0, -1):
                    if b_lst[k] > 0:
                        b_idx = k
                        break
                b_lst[b_idx] -= 1


    print(f'#{tc} {result}')