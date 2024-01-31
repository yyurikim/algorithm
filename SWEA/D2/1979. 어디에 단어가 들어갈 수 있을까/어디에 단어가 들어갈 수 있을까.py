T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    count_list = []
    for i in range(N):
        count_blank = 0
        for j in range(N):
            if lst[i][j] == 0:
                count_list.append(count_blank)
                count_blank = 0
            elif lst[i][j] == 1:
                count_blank += 1
                if j == N-1:
                    count_list.append(count_blank)

    count_blank = 0
    for j in range(N):
        count_blank = 0
        for i in range(N):
            if lst[i][j] == 0:
                count_list.append(count_blank)
                count_blank = 0
            elif lst[i][j] == 1:
                count_blank += 1
                if i == N-1:
                    count_list.append(count_blank)

    print(f'#{test_case} {count_list.count(K)}')