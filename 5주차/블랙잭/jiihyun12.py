n,m = map(int, input().split()) 
datas = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (datas[i] + datas[j] + datas[k]) <= m:
                result = max(result, (datas[i] + datas[j] + datas[k]))
print(result)
