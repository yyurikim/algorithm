import sys

input = sys.stdin.readline

p, m = map(int, input().split())

rooms = [[list(input().split())]]

for _ in range(p-1):
    player = list(input().split())

    entered = False

    for room in rooms:
        if len(room) < m and abs(int(room[0][0])-int(player[0])) <= 10:
            room.append(player)
            entered = True
            break

    if not entered:
        rooms.append([player])


for lst in rooms:
    if len(lst) == m:
        print('Started!')
    else:
        print('Waiting!')

    lst.sort(key=lambda x: x[1])

    for ply in lst:
        print(' '.join(ply))