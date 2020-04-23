import sys
r = lambda : sys.stdin.readline()
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

t = int(r().strip())

for i in range(t):
    in_data = list(map(int, r().split()))
    num = in_data[0]
    data = in_data[1:]
    ans = 0
    for j in range(0, num - 1):
        for z in range(j + 1, num):
            ans += GCD(data[j], data[z])
    print(ans)