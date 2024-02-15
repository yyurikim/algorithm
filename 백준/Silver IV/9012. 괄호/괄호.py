T = int(input())

for t in range(T):
    lst = list(map(str, input()))
    stack = []
    result = ''
    if lst[0] == ')':
        result = 'NO'
    else:
        stack.append(lst[0])
        for i in range(1, len(lst)):
            if lst[i] == '(':
                stack.append(lst[i])
            elif lst[i] == ')' and len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == ')':
                    result = 'NO'
            elif lst[i] == ')' and len(stack) == 0:
                stack.append(lst[i])
                result = 'NO'

        if len(stack) == 0:
            result = 'YES'
        else:
            result = 'NO'

    print(result)