num1, num2 = map(int, input().split())

if num1 - num2 < 0:
  print((num1-num2)*-1)
else:
  print(num1-num2)
