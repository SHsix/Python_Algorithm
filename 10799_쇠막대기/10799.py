import sys
from collections import deque

r = lambda : sys.stdin.readline().strip()

data = r()
s = deque()
ans = 0
for i in range(len(data)):
    if data[i] == '(':
        s.append(i)
    else:
        if i == s[-1] + 1:
            s.pop()
            ans += len(s)
        else:
            s.pop()
            ans += 1
print(ans)