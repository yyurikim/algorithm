import sys
input = sys.stdin.readline

N, M = map(int, input().split())

didnt_hear = set(input().strip() for _ in range(N))
didnt_see = set(input().strip() for _ in range(M))

didnt_hear_and_see = list(didnt_hear.intersection(didnt_see))

didnt_hear_and_see.sort()

print(len(didnt_hear_and_see))
for name in didnt_hear_and_see:
    print(name)