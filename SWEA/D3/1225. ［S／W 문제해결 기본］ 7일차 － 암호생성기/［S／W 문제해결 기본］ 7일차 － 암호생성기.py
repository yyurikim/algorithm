for tc in range(1, 11):
    num = int(input())
    lst = list(map(int, input().split()))

    while min(lst) > 0:
        for i in range(1,6):
            if lst[0]- i <= 0:
                lst.pop(0)
                lst.append(0)
                break
            else:
                 lst.append(lst.pop(0)-i)

    print(f'#{tc}',*lst)