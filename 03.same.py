# find same person
name = ["son", "park", "ronaldo", "henry", "park", 'herry', 'son'] 

def find_same(a): 
    n = len(a) 
    samename = set() # save result
    for i in range(0, n - 1): 
        for j in range(i + 1, n): 
            if a[i] == a[j]: 
                samename.add(a[i])
    return samename 
print(find_same(name)) 

