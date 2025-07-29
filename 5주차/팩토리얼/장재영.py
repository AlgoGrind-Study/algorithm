n = int(input())
result = 1

if 0 <= n and n <=12:
  for i in range (1, n):
    if n == 0:
      break;
    result *= (i+1)
  print(result)
