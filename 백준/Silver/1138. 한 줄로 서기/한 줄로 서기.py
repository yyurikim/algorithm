import sys

input = sys.stdin.readline

N = int(input())
# 사람들의 정보
lst = list(map(int, input().split()))
# 줄을 어떻게 서야 하는지
queue_lst = [0]*N

# 각각에 해당하는 사람 앞에 있어야 하는 키 큰 사람 수
# -> 자리를 비워 놔야 하므로 0의 수와 같음
for i in range(N):
    # zero_amt : 각 사람 앞에 있어야 하는 0의 개수
    zero_amt = lst[i]
    # cnt : queue_lst를 돌며 0의 개수를 셈
    cnt = 0
    for j in range(N):
        # 만약 키 큰 사람들이 들어갈 수 있는 자리를 확보 하고,
        # 들어가고자 하는 자리에 아직 다른 사람이 줄을 서있지 않는다면
        # 그 자리에 들어가게 되고 반복문은 break
        if cnt == zero_amt and queue_lst[j] == 0:
            queue_lst[j] = i+1
            break
        # 아직 키 큰 사람들의 자리가 확보되지 않았을 경우
        # 빈 자리가 있다면 cnt를 1 추가
        if queue_lst[j] == 0:
            cnt += 1

print(' '.join(map(str, queue_lst)))