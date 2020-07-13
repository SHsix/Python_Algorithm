def main():
    import sys
    import os
    r = lambda:sys.stdin.readline().split()
    
    N, M = map(int, r())
    go(0, M, N) # 0, 3, 1

def go(index, M, N):
    if index == M:
        print(' '.join(map(str, a[:M])), end='')
        print()
    else:
        for i in range(1, N+1):
            if c[i] == True or a[index-1] > i:
                continue
            c[i] = True
            a[index] = i
            go(index+1, M, N)
            c[i] = False

if __name__ == '__main__':
    a = [0] * 10
    c = [False] * 10
    main()
