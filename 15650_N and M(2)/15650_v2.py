def main():
    import sys

    r = lambda:sys.stdin.readline().split()
    n, m = map(int, r())
    go(1, 0, m, n)

def go(index, count, m, n):
    if count == m:
        print(' '.join(map(str, a[:m])), end='')
        print()
    else:
        if index > n:
            return
        a[count] = index
        go(index + 1, count + 1, m, n)
        a[count] = 0
        go(index+1, count, m, n)



if __name__ == '__main__':
    a = [0]*10
    c = 0
    main()