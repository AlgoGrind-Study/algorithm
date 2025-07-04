word = input()
same = True

i = 0

while i < len(word) // 2:
    front = word[i]
    back = word[len(word) -1 -i]

    if front != back:
        same = False
        break
    i = i + 1

if same == True:
    print(1)
else:
    print(0)
