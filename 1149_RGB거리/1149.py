import sys
r = lambda:sys.stdin.readline()

t = int(r().strip())
A = []
for i in range(t):
    A.append(list(map(int, r().split())))
d = [[0]*3 for _ in range(t)]
for i in range(t):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + A[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + A[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + A[i][2]

print(min(d[t-1]))