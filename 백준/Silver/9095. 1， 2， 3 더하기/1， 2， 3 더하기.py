import sys
input = sys.stdin.readline

T = int(input())

def f(n):
    if n == 1:
        result = 1
    elif n == 2:
        result = 2
    elif n == 3:
        result = 4
    else:
        result = f(n-3) + f(n-2) + f(n-1)

    return result

for _ in range(T):
    N = int(input())

    print(f(N))