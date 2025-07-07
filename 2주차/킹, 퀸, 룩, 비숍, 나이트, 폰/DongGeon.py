#3003 킹, 퀸, 룩, 비숍, 나이트, 폰
chess = [1, 1, 2, 2, 2, 8]
nums = list(map(int, input().split()))

result = ""
for i in range(len(nums)):
    result += str(chess[i] - nums[i]) + " "
print(result)
