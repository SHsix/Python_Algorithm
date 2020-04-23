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
t = int(r())
while t:
    ans_num = 0
    num = int(r())
    if num == 0:
        break

    for i in range(1, len(pn)):
        if num - pn[i] >= 2 and pn[i] <= num - pn[i]:
            if not ans[num - pn[i]]:
                ans_num += 1
    print(ans_num)

    t -= 1