T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    def get_sum(tar):
        sum_val = 0
        for i in range(len(lst)):
            if tar & 0x1:
                sum_val += lst[i]
            tar >>= 1
        return sum_val

    result = 0
    sum_val = 0

    for tar in range(1 << len(lst)):
        if get_sum(tar) == K:
            result += 1

    print(f'#{tc} {result}')