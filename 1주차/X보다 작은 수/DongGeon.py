result = ""
n,x = map(int, input().split())
nums = list(map(int, input().split()))[:n]
for i in nums:
    if i < x:
        result += str(i) + " "

print(result)
