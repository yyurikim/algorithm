import sys
input = sys.stdin.readline

stone = int(input())

if stone % 2 == 1:
    print('SK')
else:
    print('CY')