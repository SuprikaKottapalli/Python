def ChocolatesFunction(Price):
    amount = int(input("Enter the amount you have: "))
    for items in Chocolates:
        if item[0] <= amount:
            print(item[0])
    Chocolates = []
    for i in range (amount):
        ChocolateName = input("Enter Chocolate name: ")
        price = int(input("Enter the price of above chocolate: "))
        Chocolates.append([ChocolateName,price])



    


#Main
Money = int(input("Enter the amount you have: "))

menu = {25:["Kikat"],45:["Cadbary"],15:["Asha"],5:["MangoBytes"],55:["Temtations"],25:["5star"]}
for a,b in menu.items():
    if a <= Money:
        print(b)

