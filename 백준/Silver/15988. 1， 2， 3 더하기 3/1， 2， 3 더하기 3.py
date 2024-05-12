T = int(input())

lst = [1, 1, 2]
for i in range(3, 1000001):
    num = (lst[i-3] + lst[i-2] + lst[i-1])%1000000009
    lst.append(num)

for _ in range(T):
    N = int(input())
    print(lst[N])