for tc in range(1, 11):
    n = int(input())
    lst = [list(map(str, input())) for _ in range(100)]
    max_len = 0

    cnt = 0
    for word_len in range(100, 0, -1):
        for i in range(100):
            for j in range(100-word_len+1):
                word = ''.join(lst[i][j:j+word_len])
                if word == word[::-1]:
                    ans_word = word
                    cnt += 1

            if cnt == 1:
                break
        if cnt == 1:
            break

    if len(ans_word) > max_len:
        max_len = len(ans_word)


    cnt = 0
    for word_len in range(100, 0, -1):
        for i in range(100-word_len+1):
            for j in range(100):
                word = ''
                for l in range(word_len):
                    word += lst[i+l][j]
                if word == word[::-1]:
                    ans_word = word
                    cnt += 1

            if cnt == 1:
                break
        if cnt == 1:
            break

    if len(ans_word) > max_len:
        max_len = len(ans_word)

    print(f'#{tc} {max_len}')