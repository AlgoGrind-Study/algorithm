max = -1
row = 0
col = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max:
            max = row[j]
            row = i + 1 
            col = j + 1

print(max)
print(row, col)
