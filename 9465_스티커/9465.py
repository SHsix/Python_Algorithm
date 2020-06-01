import sys
r = lambda:sys.stdin.readline()
t = int(r().strip())

for _ in range(t):
    n = int(r().strip())
    number = [[0]*n for _ in range(2)]
    d = [[0]*3 for _ in range(n+1)]
    for i in range(2):
        number[i] = list(map(int, r().split()))

    for i in range(1, n+1):
        if i == 1:
            d[i][1] = number[0][0]
            d[i][2] = number[1][0]
            continue
        d[i][0] = max(d[i-1])
        d[i][1] = max(d[i-1][0], d[i-1][2]) + number[0][i-1]
        d[i][2] = max(d[i-1][0], d[i-1][1]) + number[1][i-1]

    ans = max(d[n])
    print(ans)

