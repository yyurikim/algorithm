import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = deque(map(int, input().split()))
go_line = deque()
waiting_line = deque()

go_num = 1
wait_num = N
then = 'Nice'

if lst[0] == go_num:
    go_line.append(lst.popleft())
    go_num += 1
else:
    waiting_line.append(lst.popleft())


while lst:
    num = lst[0]
    if num == go_num:
        go_line.append(lst.popleft())
        go_num += 1
    elif waiting_line and go_num == waiting_line[0]:
        go_line.append(waiting_line.popleft())
        go_num += 1
    else:
        waiting_line.appendleft(lst.popleft())


result = go_line + waiting_line

then = 'Nice'
for i in range(N-1):
    if result[i] + 1 != result[i+1]:
        then = 'Sad'
        break

print(then)