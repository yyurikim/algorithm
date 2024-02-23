

for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0


    for i in range(100):
        magnetic = ''
        for j in range(100):
            if lst[j][i] == 1 or lst[j][i] == 2:
                magnetic += str(lst[j][i])
        l = 0
        while l < len(magnetic)-1:
            if magnetic[l] == '1' and magnetic[l+1] == '2':
                cnt += 1
            l += 1

    print(f'#{tc} {cnt}')