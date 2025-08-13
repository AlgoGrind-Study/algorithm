l1, l2 = map(int, input().split())
p = l1 * l2

n1, n2, n3, n4, n5 = map(int, input().split())

nums = [n1, n2, n3, n4, n5]

for i in range (0, 5):
  nums[i] -= p
  print(nums[i], end=" ")
