import sys
def go(t):
    if t == -1:
        return
    go(v[t])
    print(A[t], end=' ')


r = lambda: sys.stdin.readline()

n = int(r().strip())
A = list(map(int, r().split()))
d = [1] * n
v = [-1] * n
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j
ans = max(d)
t = [i for i,x in enumerate(d) if x == ans][0]

print(ans)
go(t)
print()

