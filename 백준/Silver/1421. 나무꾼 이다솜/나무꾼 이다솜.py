import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
woods = []
for _ in range(N):
    woods.append(int(input()))

woods.sort(reverse=True)

max_income = 0

for wood_length in range(1, max(woods)+1):
    income = 0
    for wood in woods:
        if wood < wood_length:
            break

        max_amt = 0
        amt = 0
        cnt_of_wood= 0
        if wood % wood_length == 0:
            cnt_of_cutting = wood // wood_length - 1
            for j in range(0, cnt_of_cutting+1):
                if j == cnt_of_cutting:
                    cnt_of_wood = j+1
                else:
                    cnt_of_wood = j

                amt = cnt_of_wood*wood_length*W - C*cnt_of_cutting
                max_amt = max(amt, max_amt)
            income += max_amt
        else:
            cnt_of_cutting = wood // wood_length
            for j in range(0, cnt_of_cutting+1):
                cnt_of_wood = j
                amt = cnt_of_wood*wood_length*W - C*cnt_of_cutting
                max_amt = max(amt, max_amt)
            income += max_amt

    max_income = max(income, max_income)



print(max_income)
