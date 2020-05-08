import sys
mod = 1000000009
max = 1000001
r = lambda:sys.stdin.readline().strip()

d = [0] * max
d[0] = 1
for i in range(1, max):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]
    d[i] %= mod
t = int(r())

for _ in range(t):
    n = int(r())
    print(d[n])

