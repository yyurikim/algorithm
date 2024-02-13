fx = str(input())

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

stack = []
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

print(postfix)