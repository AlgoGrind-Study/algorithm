chars = []
sentences = []

while True:

  text = input()

  if text == "#":
    break

  if text:
    chars.append(text[0].lower())
    sentences.append(text[1:].strip().lower())

for i in range(len(chars)):

    char = chars[i]
    sentence = sentences[i]
    count = sentence.count(char)
    
    print(f"{char} {count}")
