import sys
r = lambda : sys.stdin.readline()

n = int(r().strip())
A = list(map(int, r().split()))
d = [1] * n
for i in range(0, n):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
print(max(d))
