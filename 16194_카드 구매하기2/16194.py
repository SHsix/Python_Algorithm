import sys
r = lambda : sys.stdin.readline()

n = int(r().strip())
p = [0] + list(map(int, r().split()))
d = [0] + [10000000]* (n)

for j in range(1, n+1):
    for i in range(1, j+1):
        d[j] = min(d[j], d[j-i] + p[i])
print(d[n])