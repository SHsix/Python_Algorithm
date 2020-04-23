import sys
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

r = lambda : sys.stdin.readline().split()

N, S = map(int, r())
al = list(map(int, r()))

for n, val in enumerate(al) :
    al[n] = abs(S - val)

ans = al[0]
for i in range(1, len(al)):
    ans = GCD(ans, al[i])

print(ans)