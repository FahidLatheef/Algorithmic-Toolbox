def fibonacci_last_digit(n):
    fib_lis = dict()
    for i in range(n+1):
        if (i <= 1):
            fib_lis[i] = i
        else:
            fib_lis[i] = (fib_lis[i-2] + fib_lis[i-1])%10
    return fib_lis[n]

n = int(input())
print(fibonacci_last_digit(n))
