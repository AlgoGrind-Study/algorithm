# 10807번 개수 세기
# map(function, iterable)
# function: 각 요소에 적용할 함수
# iterable: 함수를 적용할 데이터 집합
count = 0
n = int(input())
nums = list(map(int, input().split()))[:n]
v = int(input())
for i in range(len(nums)):
    if nums[i] == v:
        count += 1
print(count)
