def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
print(sum(10))

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
print(fact(4))