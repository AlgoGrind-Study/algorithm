t = int(input()) 

for i in range(t):
    money = int(input())  

    if money >= 25:
        quarter = money // 25
        money = money % 25
    else:
        quarter = 0

    if money >= 10:
        dime = money // 10
        money = money % 10
    else:
        dime = 0

    if money >= 5:
        nickel = money // 5
        money = money % 5
    else:
        nickel = 0

    penny = money

    print(quarter, dime, nickel, penny)
