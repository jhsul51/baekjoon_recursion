memo = [0]*13
def fact(n):
    global memo
    if n == 0:
        memo[n] = 1
        return memo[n]
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fact(n-1)*n
        return memo[n]
n = int(input())
print(fact(n))