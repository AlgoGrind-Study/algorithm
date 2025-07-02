pieces = [1, 1, 2, 2, 2, 8]

have = list(map(int, input().split()))

for i in range (len(pieces)):
  pieces[i] -= have[i]
  print(pieces[i], end=" ")
