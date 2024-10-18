import sys

input = sys.stdin.readline

lst = list(input().strip())

lst.sort(reverse=True)

lst = ''.join(lst)

print(lst)