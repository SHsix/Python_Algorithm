import sys

r = lambda : sys.stdin.readline()

t = int(r())
p = [0] + list(map(int, r().split()))
d = [0] * (t+1)

for i in range(1, t+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + p[j])

print(d[t])