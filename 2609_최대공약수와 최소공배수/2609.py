import sys
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

r = lambda : sys.stdin.readline().split(' ')

data = list(map(int, r()))
ans_GCD = GCD(data[0], data[1])
ans_LCM = int(data[0] * data[1] / ans_GCD)

print(ans_GCD)
print(ans_LCM)