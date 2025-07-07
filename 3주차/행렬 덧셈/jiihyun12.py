
n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    print(*row)
