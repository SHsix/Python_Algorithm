import sys
import math
def PN(a):
    if a == 1:
        return 0
    else:
        for j in range(2, int(math.sqrt(a))+1):
            if a % j == 0:
                return 0
        return 1


r = lambda: sys.stdin.readline().split()
t = r()
data = list(map(int, r()))
cnt = 0
for i in data:
    cnt += PN(i)

print(cnt)
