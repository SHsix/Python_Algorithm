import sys
MAX = 91
r = lambda : sys.stdin.readline().strip()
n = int(r())
d = [[0] * 2 for _ in range(MAX)]
d[1][1] = 1
for i in range(2, n + 1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

print(sum(d[n]))