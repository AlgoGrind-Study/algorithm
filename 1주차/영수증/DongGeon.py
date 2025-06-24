total = int(input())
num = int(input())
result = 0

for i in range(num):
    product = input().split()
    price = int(product[0])
    stock = int(product[1])
    result += int(price) * int(stock)

if result == total:
    print("Yes")
else:
    print("No")
