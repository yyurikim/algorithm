import sys

input = sys.stdin.readline

H, W = map(int, input().split())
map_lst = list(map(int, input().split()))
result = 0

for i in range(1, W-1):
    left_val = max(map_lst[:i])  # 현재 지점에서 왼쪽의 최대값
    right_val = max(map_lst[i+1:])  # 현재 지점에서 오른쪽의 최대값

    min_val = min(left_val, right_val)  # 둘 중 더 작은 값
    res_val = min_val - map_lst[i]
    
    # 주위 값에서 현재 값을 뺀 값이 0보다 클 때만 더하기
    if res_val > 0:
        result += res_val


print(result)