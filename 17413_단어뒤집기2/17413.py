from collections import deque
import sys

r = lambda : sys.stdin.readline().strip()
data = r()
ans = []
stack = deque()
n_inv = False
for ch in data:
    if ch == '<':
        n_inv = True
        if len(stack):
            while len(stack):
                ans.append(stack[-1])
                stack.pop()
    elif ch == '>':
        ans.append(ch)
        n_inv = False
        continue

    elif ch == ' ':
        if len(stack):
            while len(stack):
                ans.append(stack[-1])
                stack.pop()
            ans.append(ch)
            continue
    if n_inv:
        ans.append(ch)
    else:
        stack.append(ch)

if len(stack):
    while len(stack):
        ans.append(stack[-1])
        stack.pop()

print(''.join(map(str, ans)))


