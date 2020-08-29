def fibonacci_sum_ll(n):
    fib_lis = dict()
    for i in range(n+1):
        if (i <= 1):
            fib_lis[i] = i
        else:
            fib_lis[i] = fib_lis[i-2] + fib_lis[i-1]
    return fib_lis

sum_ld = []
for i in range(60):
    d = fibonacci_sum_ll(i)
    sum_ld.append(sum(d.values())%10)

m, n = map(int, input().split())
last_digit_mapping = sum_ld[int(n%60)]-sum_ld[int((m-1)%60)]
# Since sum(fib30-80) = sum(fib0-80) - sum(fib0-30)
print(last_digit_mapping%10) #takes care of negative integers
#print(sum_ld)
