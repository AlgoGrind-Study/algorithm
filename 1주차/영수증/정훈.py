num1 = int(input())
num2 = int(input())
sum =0

for i in range(num2):
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    sum += (a * b)
if sum == num1:
    print('Yes')
else:
    print('No')
