import sys
r = lambda:sys.stdin.readline().strip()
tall = []

tall = [int(r()) for _ in range(9)]

tall = sorted(tall)
t_sum = sum(tall)

for i in range(8):
    for j in range(i+1, 9):
        tmp = t_sum - tall[i] - tall[j]
        if tmp == 100:
            for ans in range(9):
                if ans == i or ans == j:
                    continue
                print(tall[ans])
            sys.exit(0)


