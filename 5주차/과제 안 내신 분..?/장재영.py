n = set()
m = []
for i in range(28):
  k = int(input())
  n.add(k)

m = set(range(1, 31))
x = sorted(list(m - n))

for j in x:
  print(j)
