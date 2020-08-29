def gcd(a, b):
    if a < b:
        a,b = b,a
    c = a%b
    while c != 0:
        a,b = b,c
        c = a%b
    return b


a, b = map(int, input().split())
print(gcd(a, b))
