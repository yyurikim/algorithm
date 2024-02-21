import sys
input = sys.stdin.readline
cnt = 0
N = int(input())
switch = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    student, number = map(int,input().split())
    # 남학생일 때
    if student == 1:
        # 자기가 받은 수의 배수인 스위치의 상태를 바꾼다
        multi_num = 1
        while (number*multi_num-1) <= N-1:
            if switch[number*multi_num-1] == 1:
                switch[number*multi_num-1] = 0
            else:
                switch[number*multi_num-1] = 1
            multi_num += 1

    # 여학생일 때
    elif student == 2:
        switch[number-1] = abs(switch[number-1]-1)
        side_num = 1
        while (number-side_num-1>=0 and number+side_num-1<N) and (switch[number-1-side_num] == switch[number-1+side_num]):
            switch[number-side_num-1] = abs(switch[number-side_num-1]-1)
            switch[number+side_num-1] = abs(switch[number+side_num-1]-1)
            side_num += 1


result = ""
for i in range(0, N):
    if i!=0 and i%20==0:
        result+="\n"
    result+=f"{switch[i]} "

print(result)