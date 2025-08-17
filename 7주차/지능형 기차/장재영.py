out = []
inn = [] 

for i in range(4):
  a, b = map(int, input().split())
  out.append(a)
  inn.append(b)

hot = inn[0]
people = inn[0]

for j in range(1, 3):
  people += inn[j] - out[j]
  if hot < people:
    hot = people

print(hot)
