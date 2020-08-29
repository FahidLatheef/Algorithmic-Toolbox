def pisano_pattern(m):
    pis_lis = dict()
    key = 0
    for i in range(10000):

        if (i <= 1):
            pis_lis[i] = i
        else:
            pis_lis[i] = (pis_lis[i-1] + pis_lis[i-2])%m

        if len(pis_lis)>2 and pis_lis[i]==1 and pis_lis[i-1]==0:
            key = i
            break

    del pis_lis[key]
    del pis_lis[key-1]

    return pis_lis, len(pis_lis)

n, m = map(int, input().split())
dic, length = pisano_pattern(m)
print(dic[int(n%length)])

