# 2739

N = int(input("숫자를 입력하세요(1~9)")) 

if 1 <= N <= 9:
    for i in range(1,10):
        result = N * i
        print(f'{N} * {i} = {result}')
else:
    print("1이상 9이하의 숫자만 입력하세요")

