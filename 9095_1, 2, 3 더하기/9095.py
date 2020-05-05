import sys
r = lambda : sys.stdin.readline().strip()

t = int(r())
d = [1] + [0] * 10
for i in range(1, 11):
    if i-1 >= 0:
        d[i] += d[i-1]
    if i-2 >= 0:
        d[i] += d[i-2]
    if i-3 >= 0:
        d[i] += d[i-3]

while t :
    n = int(r())
    print(d[n])
    t -= 1

