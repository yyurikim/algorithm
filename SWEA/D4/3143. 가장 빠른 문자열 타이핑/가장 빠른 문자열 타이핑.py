T = int(input())

for tc in range(1, T+1):
    txt, pat = map(str, input().split())
    cnt = 0
    idx = 0
    len_txt = len(txt)
    len_pat = len(pat)


    while idx < len_txt:
        if txt[idx : idx+len_pat] == pat:
            cnt += 1
            idx += len_pat
        else:
            cnt += 1
            idx += 1

    print(f'#{tc} {cnt}')