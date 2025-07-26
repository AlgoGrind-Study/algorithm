x1, y1, n1, x2, y2, n2 = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if x1 * x + y1 * y == n1 and x2 * x + y2 * y == n2:
            print(x, y)
