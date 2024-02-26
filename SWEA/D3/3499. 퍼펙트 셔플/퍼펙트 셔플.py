import math
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    lst = list(map(str, input().split()))

    a = 0
    b = math.ceil(N/2)

    print(f'#{tc}', end = ' ')

    for i in range(b):
        print(lst[a], end = ' ')
        a += 1
        if b <= N-1:
            print(lst[b], end = ' ')
            b += 1
    print()