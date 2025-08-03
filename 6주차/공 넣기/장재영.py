n, m = map(int, input().split())
counts = []

for i in range (n):
  counts.append(0)

for j in range (m):
  a, b, c = map(int, input().split())
  for k in range(a - 1, b):
        counts[k] = c

print(*counts)
