# 2738번 행렬 덧셈
n, m = map(int, input().split())

# 리스트 생성
a = []
b = []

for _ in range(n):
    nums = list(map(int, input().split()))
    a.append(nums)

for _ in range(n):
    nums = list(map(int, input().split()))
    b.append(nums)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()
