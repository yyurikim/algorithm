def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        if par[T] == '+':
            par[T] = int(par[left[T]]) + int(par[right[T]])
        elif par[T] == '-':
            par[T] = int(par[left[T]]) - int(par[right[T]])
        elif par[T] == '*':
            par[T] = int(par[left[T]]) * int(par[right[T]])
        elif par[T] == '/':
            par[T] = int(par[left[T]]) / int(par[right[T]])

for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)

    node_info = [list(input().split()) for _ in range(N)]

    for j in range(N):
        par[int(node_info[j][0])] = node_info[j][1]
        if len(node_info[j]) >2:
            left[int(node_info[j][0])] = int(node_info[j][2])
            right[int(node_info[j][0])] = int(node_info[j][3])

    print(f'#{tc}', end = ' ')
    post_order(1)
    print(int(par[1]))