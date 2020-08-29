n = int(input())
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
maxer = [i*j for i,j in zip(sorted(lis1), sorted(lis2))]
print(sum(maxer))
