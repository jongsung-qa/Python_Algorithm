# sum 1 ~ 10
def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
print(sum(10))

# factorial(5! = 5*4*3*2*1)
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
print(fact(4))

# sum 1 ~ 100
def sum1(n):
    return n*(n+1)//2
print(sum1(100))



