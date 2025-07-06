#5622번 다이얼
number = input()

# match ~ case
def dial(number):
    match number:
        case "A" | "B" | "C":
            return 3
        case "D" | "E" | "F":
            return 4
        case "G" | "H" | "I":
            return 5
        case "J" | "K" | "L":
            return 6
        case "M" | "N" | "O":
            return 7
        case "P" | "Q" | "R" | "S":
            return 8
        case "T" | "U" | "V":
            return 9
        case "W" | "X" | "Y" | "Z":
            return 10
            
result = 0
for i in number:
    result += dial(i)
print(result)
