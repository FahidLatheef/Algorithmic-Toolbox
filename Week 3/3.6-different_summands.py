import math
n = int(input())
a = 1
b = 1
c = -2*n
# Recall p(p+1)/2
# quadratic : p**2 + p - 2*n = 0
# (-b +- sqrt(b**2-4ac))/2a
d = math.sqrt(b**2 - 4*a*c)
solution = (-1+d)/2  # other solution is negative
k = math.floor(solution)
print(k)
summ = []
for i in range(k-1):
    summ.append(i+1)
last = n-sum(summ)
summ.append(last)

for _ in summ:
    print(_, sep="", end=" ")
