n, x = map(int, input().split())
nums = list(map(int, input().split()))

for i in range (0, len(nums)):
  if nums[i] < x:
    print(f"{nums[i]}", end=" ")
