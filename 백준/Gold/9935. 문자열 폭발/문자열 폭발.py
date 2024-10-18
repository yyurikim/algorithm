import sys

input = sys.stdin.readline

word = input().strip()
target = input().strip()

stack = []

for alp in word:
    stack.append(alp)

    if len(stack) >= len(target) and ''.join(stack[-len(target):]) == target:
        for _ in range(len(target)):
            stack.pop()


if stack:
    print(''.join(stack))
else:
    print('FRULA')