nums = []
max = -1
row = 0
column = 0

for i in range (9):
  numbers = list(map(int, input().split()))
  nums.append(numbers)

for j in range (9):
  for k in range (9):
    if max < nums[j][k]:
      max = nums[j][k]
      row = j + 1
      column = k + 1

print(max)
print(f'{row} {column}')
