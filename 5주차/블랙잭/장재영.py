count, m = map(int, input().split())
cards = list(map(int, input().split()))

nums = []

for i in range (count):
  for j in range (i+1, count):
    for k in range (j+1, count):
      if (cards[i] + cards[j] + cards[k] <= m):
        nums.append(cards[i] + cards[j] + cards[k])

result = nums[0]

for l in range (len(nums)):
  if (result < nums[l]):
    result = nums[l]

print(result)
