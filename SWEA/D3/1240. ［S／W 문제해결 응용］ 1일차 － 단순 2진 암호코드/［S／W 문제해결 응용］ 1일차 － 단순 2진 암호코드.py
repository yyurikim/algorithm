code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(N)]

    for i in range(M):
        if '1' in lst[i]:
            row_idx = i
            break

    for j in range(M-1, 0, -1):
        if lst[row_idx][j] == '1':
            col_idx = j
            break

    temp = lst[row_idx][col_idx-55 : col_idx+1]
    password = []

    for l in range(0, 56, 7):
        password.append(code[''.join(temp[l:l+7])])

    odd_sum = 0
    even_sum = 0

    for i in range(1,9):
        if i % 2 == 1:
            odd_sum += password[i-1]
        else:
            even_sum += password[i-1]

    if (odd_sum*3 + even_sum) % 10 == 0:
        print(f'#{tc} {sum(password)}')
    else:
        print(f'#{tc} 0')