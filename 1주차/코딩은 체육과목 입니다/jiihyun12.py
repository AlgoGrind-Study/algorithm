# 25314

n = int(input())  
count = n // 4    

l_long = "long "
i_int = "int" 
result = ""

for i in range(count):  
    result += l_long

result += i_int 

print(result)

================================

#오답 노트
n / 4 -> float반환
n // 4 -> int 반환
