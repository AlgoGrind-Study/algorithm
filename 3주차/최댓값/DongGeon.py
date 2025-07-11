max_value = -1
row_index = 0
col_index = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            row_index = i + 1 
            col_index = j + 1

print(max_value)
print(row_index, col_index)
