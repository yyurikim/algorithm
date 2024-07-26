import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
conveyor = deque(map(int, input().split()))
robot = deque([0]*N)

# 단계
level = 0

# 내구도가 0인 칸의 개수가 K개 미만일 때까지만 반복
while (conveyor.count(0) < K):
    # 이전 과정을 다 수행했으면 1단계 추가
    level += 1
    # 1.벨트가 한 칸 회전 -> 로봇 위치도 변경
    conveyor.rotate(1)
    robot.rotate(1)
    ## 내리는 위치에 도달한 로봇은 내려줌
    robot[N-1] = 0

    # 2. 로봇의 회전
    ## 내리는 위치가 아닌 로봇들의 경우,
    ## 먼저 올라간 로봇 즉 N-1에 가까운 순부터 이동.
    ## 이동하고자 하는 위치의 내구도가 0 이상이고 로봇이 없을 경우에만 이동
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and conveyor[i+1] > 0 and robot[i+1] == 0:
            robot[i] = 0
            robot[i+1] = 1
            conveyor[i+1] -= 1
    ## 내리는 위치에 도달한 로봇은 내려줌
    robot[N-1] = 0

    # 3. 새로운 로봇 올리기
    if conveyor[0] > 0 and robot[0] == 0:
        robot[0] = 1
        conveyor[0] -= 1

print(level)