import sys

r = lambda:sys.stdin.readline().split()

data = list(map(int, r()))
pn = []
ans = [False] * (data[1] + 1)
for i in range(2, data[1] + 1):
    if not ans[i]:
       pn.append(i)
       for j in range(i + i, data[1] + 1, i):
           ans[j] = True
for num in pn:
    if num >= data[0]:
        print(num)


# m, n = map(int, input().split())
# arr = [False, False] + [True] * (1000000 - 1)
#
# for i, el in enumerate(arr):
#     if el:
#         for _ in range(i*2, 1000000, i):
#             arr[_] = False
#
# for i in range(m, n+1):
#     if arr[i]:
#         print(i)