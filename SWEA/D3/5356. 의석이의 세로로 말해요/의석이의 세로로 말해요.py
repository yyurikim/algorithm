T = int(input())
for tc in range(1, T+1):
    lst = list(str(input()) for _ in range(5))
    words_len = 0
    max_len = 0
    for i in range(5):
        words_len += len(lst[i])
        if len(lst[i]) > max_len:
            max_len = len(lst[i])

    result = ''
    cnt = 0

    while cnt < words_len:
        for j in range(max_len):
            for k in range(5):
                if j < len(lst[k]):
                    result += lst[k][j]
                    cnt += 1

    print(f'#{tc} {result}')