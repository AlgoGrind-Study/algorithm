nums = [1,1,2,2,2,8]
count = list(map(int, input().split()))
reuslt = []

for i in range(6):
    reuslt.append(nums[i] - count[i])
print(*reuslt)
