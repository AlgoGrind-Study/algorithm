# 10871

n, x = map(int, input().split())
a = list(map(int, input().split()))

result = '' 

for i in a:
    if i < x:
        result += str(i) + ' ' 

print(result)
