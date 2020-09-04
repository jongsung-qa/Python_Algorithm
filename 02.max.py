# find max

a = [1,5,3,30,21,7]

def max(a):
    n = len(a)
    max_v = a[0] # 1st value => max_v
    for i in range(1,n):
        if a[i] > max_v: # compare value
            max_v = a[i]
    return max_v
print(max(a))
