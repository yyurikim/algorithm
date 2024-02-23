import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    amt = int(input())
    Q = amt // 25
    amt = amt - (Q*25)
    D = amt // 10
    amt = amt - (D*10)
    N = amt // 5
    amt = amt - (N*5)
    P = amt // 1
    amt = amt - (1*5)

    print(Q, D, N, P)