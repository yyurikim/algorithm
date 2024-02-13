N = int(input())
loc_lst = []
paper_lst = [[0]*101 for _ in range(101)]
cnt = 0
for i in range(N):
    nums = list(map(int, input().split()))
    loc_lst.append(nums)

for idx in range(len(loc_lst)):
    for j in range(10):
        for k in range(10):
            paper_lst[loc_lst[idx][0]+j][loc_lst[idx][1]+k] = 1

for i in range(101):
    for j in range(101):
        if paper_lst[i][j] == 1:
            cnt += 1

print(cnt)