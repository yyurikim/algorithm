import sys
input = sys.stdin.readline

N = int(input())
card_lst = list(map(int, input().split()))
M = int(input())
num_lst = list(map(int, input().split()))

num_dict = {}

for i in num_lst:
    num_dict[i] = 0

for j in card_lst:
    if j in num_dict:
        num_dict[j] += 1


for k in num_lst:
    print(num_dict[k], end=' ')