# 01.sum 1 ~ 100

def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
print(sum(10))


