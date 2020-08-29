n = int(input())
lis = list(map(int,input().strip().split()))
max1 = max(lis)
lis.remove(max1)
max2 = max(lis)
print(max1*max2)


    
    
    
    
