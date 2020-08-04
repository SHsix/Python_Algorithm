import sys
r = lambda : sys.stdin.readline()

l, c = map(int, r().split())

char = r().split()

char = sorted(char)
def check(pwd):
    a = 0
    b = 0
    for ch in pwd:
        if ch == 'a' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'e':
            a += 1
        else:
            b += 1
    if a >= 1 and b >= 2:
        return True
    else:
        return False

def go(n, alpha, pwd, i):
    if len(pwd) == n:
        if check(pwd):
            print(''.join(map(str, pwd)))
    if len(pwd) > n or i > len(alpha) - 1 :
        return
    if len(pwd) < n:
        pwd.append(alpha[i])
        go(n, alpha, pwd, i+1)
        pwd.pop()
        go(n, alpha, pwd, i+1)
pwd = list()
go(l, char, pwd, 0)
