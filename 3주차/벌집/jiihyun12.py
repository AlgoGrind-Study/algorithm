n = int(input())

floor = 1
num = 1

while n > num:
    num += 6 * floor
    floor += 1
    
print(floor)
