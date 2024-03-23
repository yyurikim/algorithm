import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info_dict = {}
for i in range(1, N+1):
    info_dict[input().strip()] = str(i)

info_dict_rev = dict(map(reversed, info_dict.items()))

for _ in range(M):
    pokemon = input().strip()
    if pokemon.isdecimal():
        print(info_dict_rev[pokemon])
    else:
        print(info_dict[pokemon])