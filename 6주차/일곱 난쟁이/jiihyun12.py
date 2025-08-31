
heights = [int(input().strip()) for _ in range(9)]

total = sum(heights)
need = total - 100

seen = set()
fake_a = None
fake_b = None

for h in heights:
    complement = need - h
    if complement in seen:
        fake_a = h
        fake_b = complement
        break
    seen.add(h)

answer = heights[:]
answer.remove(fake_a)
answer.remove(fake_b)

for x in sorted(answer):
    print(x)
