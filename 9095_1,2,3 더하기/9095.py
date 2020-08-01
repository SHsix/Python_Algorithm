import sys

r = lambda:sys.stdin.readline()

t = int(r().strip())


def go(sum, goal):
    now = 0
    if sum > goal:
        return now
    if sum == goal:
        return 1
    if sum < goal:
        for i in range(1, 4):
            now += go(sum + i, goal)

    return now

for _ in range(t):
    n = int(r().strip())
    print(go(0, n))

