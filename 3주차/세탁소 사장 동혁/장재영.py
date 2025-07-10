count = int(input())
nums = []
quarter = 0
dime = 0
nickel = 0
penny = 0

for i in range (count):
  num = int(input())
  nums.append(num)

for j in range (count):
  quarter = int(nums[j] / 25)
  dime = int(nums[j] % 25 / 10)
  nickel = int(nums[j] % 25 % 10 / 5)
  penny = int(nums[j] % 25 % 10 % 5)
  print(f'{quarter} {dime} {nickel} {penny}')
