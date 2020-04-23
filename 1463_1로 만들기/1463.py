import sys
r = lambda : sys.stdin.readline().strip()

N = int(r())
mem = [0] * (N + 1)
mem[1] = 0

for i in range(2, N + 1):
    mem[i] = mem[i-1] + 1
    if i % 2 == 0 and mem[i] > mem[i//2] + 1:
        mem[i] = mem[i//2] + 1
    if i % 3 == 0 and mem[i] > mem[i//3] + 1:
        mem[i] = mem[i//3] + 1

print(mem[N])