T = int(input())

for tc in range(1, T+1):
    bin_num = input()
    tri_num = input()
    bin_lst = list(bin_num)
    bin_to_num = []

    for i in range(1, len(bin_num)):
        bin_lst[i] = str(1 - int(bin_lst[i]))
        bin_to_num.append(''.join(bin_lst))
        bin_lst[i] = str(1 - int(bin_lst[i]))

    for n in bin_to_num:
        num = int(n, 2)
        temp = num
        tri_compare = ''
        while temp:
            tri_compare += str(temp % 3)
            temp = temp // 3
        tri_compare = tri_compare[::-1]

        if len(tri_compare) == len(tri_num):
            cnt = 0
            for k in range(len(tri_num)):
                if tri_num[k] != tri_compare[k]:
                    cnt += 1
            if cnt == 1:
                print(f'#{tc} {num}')
                break