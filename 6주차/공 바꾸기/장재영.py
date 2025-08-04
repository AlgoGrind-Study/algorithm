n, m = map(int, input().split())
nums = []

for a in range (0, n):
  nums.append(a+1)

for b in range (m):
  i, j = map(int, input().split())
  c = nums[i-1]
  d = nums[j-1]
  nums[j-1] = c
  nums[i-1] = d

print(*nums)
