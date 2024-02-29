T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))

    customer.sort()
    cnt = 0
    result = 'Possible'

    for i in range(len(customer)):
        bung = (customer[i] // M) * K - cnt
        if bung > 0:
            cnt += 1
        else:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')