t = int(input())
words = []
length = []

for i in range (t):
  word = input()
  words.append(word)

for j in range (len(words)):
  length.append(len(words[j]))

for k in range (0, t):
  print(f'{words[k][0]}{words[k][length[k]-1]}')
