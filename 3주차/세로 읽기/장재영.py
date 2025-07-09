letters = []
length = 0
result = ''

for i in range (5):
  letter = input()
  letters.append(letter)
  if len(letter) > length:
    length = len(letter)

for j in range (length):
  for k in range (5):
    if j < len(letters[k]):
            result += letters[k][j]

print(result)
