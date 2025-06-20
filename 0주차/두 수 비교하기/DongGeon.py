num = str(input())
split_num = num.split()
A = int(split_num[0])
B = int(split_num[1])

if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
