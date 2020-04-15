import sys
from collections import deque
r = lambda : sys.stdin.readline().split()
t = r()
data = list(map(int, r()))
s = deque()
s.append(0)
ans = [0] * len(data)
for i in range(1, len(data)):
    if not s:
        s.append(i)
    while s and data[s[-1]] < data[i]:
        ans[s[-1]] = data[i]
        s.pop()
    s.append(i)

for i in s:
    ans[i] = -1

print(' '.join(map(str, ans)))