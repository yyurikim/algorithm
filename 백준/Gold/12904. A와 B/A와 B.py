import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()

while len(S)<len(T):

    if T[-1] == 'A':
        T = T[:-1]

    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]


if T == S:
    print(1)
else:
    print(0)