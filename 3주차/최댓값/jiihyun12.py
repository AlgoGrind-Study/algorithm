max_num = -1
max_row = 0
max_col = 0

row_num = 1
while row_num <= 9:
    line = input().split()
  
    col_num = 1

    for num in line: 
        num = int(num)

        if num > max_num:
            max_num = num
            max_row = row_num
            max_col = col_num

        col_num += 1  
      
    row_num += 1 
print(max_num)
print(max_row, max_col)
