#10988 팰린드롬인지 확인하기
word = input()
reversed_word = word[::-1]
result = 1

for i in range(len(word)):
    if word[i] == reversed_word[i]:
        continue
    else:
        result = 0
        break
print(result)
