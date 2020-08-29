def fibonacci_sum_ll(n):
    fib_lis = dict()
    for i in range(n+1):
        if (i <= 1):
            fib_lis[i] = i
        else:
            fib_lis[i] = fib_lis[i-2] + fib_lis[i-1]
    return fib_lis

sum_ld = []
for i in range(60):#60 reps found
    d = fibonacci_sum_ll(i)
    sum_ld.append(sum(d.values())%10)

n = int(input())
print(sum_ld[int(n%60)])
