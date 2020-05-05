import sys
div = 1000000009
limit = 100000
r = lambda : sys.stdin.readline().strip()

d = [[0]*4 for _ in range(limit + 1)]

for i in range(1, limit + 1):
    if i - 1 >= 0:
        d[i][1] = d[i-1][2] + d[i-1][3]
        if i == 1:
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i == 3:
            d[i][3] = 1
    for j in range(1, 4):
        d[i][j] %= div

t = int(r())
while t:
    n = int(r())
    print(sum(d[n])%div)
    t -= 1