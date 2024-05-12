import sys
input = sys.stdin.readline

N = int(input())

lst = [0] * 31

lst[2] = 3

if N % 2 != 0:
    print(0)
else:
    for i in range(4, N+1, 2):
        lst[i] = lst[i-2]*3 + sum(lst[:i-3])*2 + 2
    print(lst[N])