import sys

r = lambda : sys.stdin.readline()

n = int(r().strip())
d = [[0] * 2 for _ in range(n)]

for i in range(n):
    d[i] = list(map(int, r().split()))
ans = 0
def go(day, sum):
    global ans
    if day > n:
        return
    if day == n:
        ans = max(ans, sum)
        return

    go(day+1, sum)
    go(day+d[day][0], sum + d[day][1])

go(0, 0)
print(ans)
