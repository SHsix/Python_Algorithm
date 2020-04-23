import sys
r = lambda : sys.stdin.readline().strip()
MAX = 1000000
ans = [False, False] + [False] * (MAX - 1)
pn = []
for i in range(2, MAX + 1):
    if not ans[i]:
        pn.append(i)
        for j in range(i + i, MAX + 1, i):
            ans[j] = True

while True:
    num = int(r())
    if num == 0:
        break
    for i in range(1, len(pn)):
        if not ans[num - pn[i]]:
            print('{0} = {1} + {2}'.format(num, pn[i], num - pn[i]))
            break