n = int(input())

result = 0

for m in range(1, n + 1):       
    value = sum(map(int, str(m)))  
    if m + value == n:             
        result = m                
        break                    

print(result)
