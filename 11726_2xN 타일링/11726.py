MAX = 1000
Div = 10007
T = [0] * (MAX + 1)
T[1] = 1
T[2] = 2

n = int(input())
for i in range(3, n + 1):
    T[i] = (T[i - 1]%Div) + (T[i - 2]%Div)

print(T[n]%Div)

