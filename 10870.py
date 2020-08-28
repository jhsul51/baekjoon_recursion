memo = [-1]*21
def fib(n):
    if n == 0:
        memo[n] = 0
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

n = int(input())
print(fib(n))