import sys
input = sys.stdin.readline

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

k1= t-(w-p)
k2 = t-(h-q)

if k1 >= 0:
    if (k1//w) % 2 == 1:
        result1 = k1 % w
    elif (k1//w) % 2 == 0:
        result1 = w - (k1 % w)
else:
    result1 = p + t

if k2 >= 0:
    if (k2//h) % 2 == 1:
        result2 = k2 % h
    elif (k2//h) % 2 == 0:
        result2 = h - (k2 % h)
else:
    result2 = q + t

print(result1, result2)