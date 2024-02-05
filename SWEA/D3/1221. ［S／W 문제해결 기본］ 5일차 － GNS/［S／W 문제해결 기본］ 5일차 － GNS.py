T = int(input())

num_dict = {"ZRO" : 0, "ONE" : 1, "TWO":2, "THR": 3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

for tc in range(1, T+1):
    N, L = map(str, input().split())
    leng = int(L)
    lst = list(map(str, input().split()))

    num_lst = [0]*leng

    for i in range(leng):
        num_lst[i] = num_dict[lst[i]]

    num_lst.sort()

    for j in range(leng):
        for key, value in num_dict.items():
            if value == num_lst[j]:
                num_lst[j] = key

    print(f'#{tc}', *num_lst)