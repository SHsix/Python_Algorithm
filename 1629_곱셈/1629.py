import sys


r = lambda:sys.stdin.readline().split()
A, B, C = map(int, r())

print(pow(A,B,C))

def pow(A, B, C):
    if B == 0:
        return 1
    ans = pow(A%C, B/2)
    if B % 2 == 0:
        return ans*ans%C
    else:
        return ans*ans*A%C
