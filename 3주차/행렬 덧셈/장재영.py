row, column = map(int, input().split())

a = []
b = []

for i in range (row):
  nums = list(map(int, input().split()))
  a.append(nums)

for j in range (row):
  nums = list(map(int, input().split()))
  b.append(nums)

for k in range (row):
  for l in range (column):
    print(a[k][l]+b[k][l], end=' ')
  print('')
