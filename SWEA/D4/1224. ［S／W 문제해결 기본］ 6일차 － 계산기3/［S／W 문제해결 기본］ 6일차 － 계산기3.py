for tc in range(1, 11):
    len_val = int(input())
    fx = str(input())

    # 후위 표기식으로 변환
    stack = []
    top = -1

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    postfix = ''

    for tk in fx:
        if tk == '(' or (len(stack) == 0 and tk in '*/+-') or (stack and tk in '*/+-' and isp[stack[-1]] < icp[tk]):
            stack.append(tk)
        elif stack and tk in '*/+-' and isp[stack[-1]] >= icp[tk]:
            while len(stack) > 0 and isp[stack[-1]] >= icp[tk]:
                postfix += stack.pop()
            stack.append(tk)
        elif tk == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            postfix += tk

    while stack:
        postfix += stack.pop()


    # 변환된 식 계산
    lst = []
    result = 0

    for tk in postfix:
        if tk.isdecimal():
            lst.append(tk)
        elif tk in '+*':
            n1 = int(lst.pop())
            n2 = int(lst.pop())
            if tk == '+':
                lst.append(n2 + n1)
            if tk == '*':
                lst.append(n2 * n1)

    print(f'#{tc} {lst.pop()}')
