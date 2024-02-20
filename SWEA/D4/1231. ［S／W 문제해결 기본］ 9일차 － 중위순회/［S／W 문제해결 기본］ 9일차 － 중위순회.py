def inorder(T):
    if T:
        inorder(left[T])
        print(node_info[T-1][1], end='')
        inorder(right[T])

for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)

    node_info = [list(input().split()) for _ in range(N)]

    for j in range(N):
        if len(node_info[j]) >= 3:
            left[int(node_info[j][0])] = int(node_info[j][2])
            if len(node_info[j]) == 4:
                right[int(node_info[j][0])] = int(node_info[j][3])
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()