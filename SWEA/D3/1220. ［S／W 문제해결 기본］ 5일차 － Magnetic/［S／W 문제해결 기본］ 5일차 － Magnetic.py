for tc in range(1, 11):
    cnt = 0
    N = int(input())
    lst = [list(map(str, input().split())) for _ in range(N)]
    lst_re = list(zip(*lst))
    cnt = 0
    for st in lst_re:
        st = ''.join(st)
        st = st.replace('0', '')
        cnt += st.count('12')


    print(f'#{tc} {cnt}')