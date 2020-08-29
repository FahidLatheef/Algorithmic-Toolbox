def fibonacci_sum(n):
    fib_lis = []
    for i in range(n+1):
        if (i <= 1):
            fib_lis.append(i)
        else:
            fib_lis.append(fib_lis[i-2] + fib_lis[i-1])
    return fib_lis

sum_ld = []
for i in range(30): #By trial and error found 30 reps
    sum_ld.append(sum(i**2 for i in fibonacci_sum(i))%10)

n = int(input())
print(sum_ld[int(n%30)])
#print(sum_ld,sep = "", end = " ")
