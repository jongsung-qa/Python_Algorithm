# find same person
def find_same_name(a): n = len(a) # 리스트의 자료 개수를 n에 저장 
samename = set() # 결과를 저장할 빈 집합 
for i in range(0, n - 1): # 0부터 n-2까지 반복 
    for j in range(i + 1, n): # i+1부터 n-1까지 반복 
        if a[i] == a[j]: # 이름이 같다면? 
            samename.add(a[i]) # 찾은 이름을 result에 추가 
            return samename name = ["박지성", "차두리", "김남일", "박지성"] 
print(find_same_name(name)) 

name2 = ["박지성", "차두리", "김남일", "박지성"]
print(find_same_name(name2))

