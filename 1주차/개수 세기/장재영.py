length = int(input())
count = 0
nums = list(map(int, input().split()))
num = int(input())

for i in range (0, len(nums)):
  if nums[i] == num:
    count += 1
print(count)
