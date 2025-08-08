heights = []
p = 0

for i in range(0, 9):
  p = int(input())
  heights.append(p)

total = sum(heights)
heights.sort()

for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            for h in heights:
                if h != heights[i] and h != heights[j]:
                    print(h)
            exit()
