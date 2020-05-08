import sys
mod = 10007
r = lambda:sys.stdin.readline().strip()
n = int(r())
d = [[0]*10 for _ in range(n+1)]
d[1] = [1]*10
for i in range(2, n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:10]) % 10007

print(sum(d[n]) % 10007)