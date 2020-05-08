import sys

r = lambda : sys.stdin.readline()

t = int(r().strip())
A = list(map(int, r().split()))
d = [0] * t
for i in range(t):
    d[i] = A[i]
    if i == 0:
        continue
    if A[i]+d[i-1] > d[i]:
        d[i] = A[i]+d[i-1]

print(max(d))