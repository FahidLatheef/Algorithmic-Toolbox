def lcs3(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    subs = [[[0 for k in range(n + 1)] for j in range(l + 1)] for i in range(m + 1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i + 1][j + 1][k + 1] = subs[i][j][k] + 1
                else:
                    subs[i + 1][j + 1][k + 1] = max(subs[i + 1][j + 1][k],
                                                    subs[i][j + 1][k + 1],
                                                    subs[i + 1][j][k + 1])
    return subs[-1][-1][-1]


int(input())
a = list(map(int, input().split()))
int(input())
b = list(map(int, input().split()))
int(input())
c = list(map(int, input().split()))

print(lcs3(a, b, c))
