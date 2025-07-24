num = int(input())
result = 0

for i in range(1, num):
  result = i + sum(map(int, str(i)))

  if result == num:
    print(i)
    break

else:
  print(0)
