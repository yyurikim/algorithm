import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info_dict = {}
for _ in range(N):
    url, password = input().split()
    info_dict[url] = password

for _ in range(M):
    print(info_dict[input().strip()])