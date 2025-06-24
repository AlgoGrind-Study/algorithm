total = int(input())
count = int(input())

for i in range(0, count):
  money, num = map(int, input().split())
  total -= money * num

if total == 0:
  print('Yes')
else:
  print('No')
