import sys
mod = 9901
r = lambda:sys.stdin.readline().strip()
n = int(r())
d = [[0]*3 for _ in range(n+1)]
d[1] = [1, 1, 1]
for i in range(2, n+1):
    d[i][0] = d[i-1][1]+d[i-1][2]%mod
    d[i][1] = d[i-1][0]+d[i-1][2]%mod
    d[i][2] = sum(d[i-1])%mod

print(sum(d[n])%mod)