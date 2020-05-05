import sys
mod = 1000000000
r = lambda : sys.stdin.readline()

d = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j - 1 >= 0:
            d[i][j] += d[i-1][j-1]
        if j + 1 < 10:
            d[i][j] += d[i-1][j+1]
n = int(r())
print(sum(d[n])%mod)