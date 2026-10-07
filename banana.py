def banana():
    bananaPrice = 120
    bananaQuantity = 20
    bananaTotal = 0
    bananaReq= int(input(f"There are {bananaQuantity} dozens of bananas, each dozen cost {bananaPrice} pkr. How much do you want: "))
    bananaQuantity = bananaQuantity - bananaReq
    bananaTotal  = bananaPrice * bananaReq
    if bananaReq >= bananaQuantity :
        print("There are not enough dozens of bananas")
        return 0
    else:
        print(f"Thanks for buying. You total price of Bananas are {bananaTotal}")
    return bananaTotal

def apple():
    applePrice = 200
    appleQuantity = 25
    appleTotal = 0
    appleReq= int(input(f"There are {appleQuantity} kilograms of apple, each kilos cost {applePrice} pkr. How much do you want: "))
    appleQuantity = appleQuantity - appleReq
    appleTotal = applePrice * appleReq
    if appleReq > appleQuantity :
        print("There are not enough kilos of apples")
        return 0
    else:
        print(f"Thanks for buying. You total price of Apples are {appleTotal}")
    return appleTotal

def watermelon():
    watermelonPrice = 110
    watermelonQuantity = 20
    watermelonTotal = 0
    watermelonReq = int(input(f"There are {watermelonQuantity} kilograms of watermelon, each kilo cost {watermelonPrice} pkr."))
    watermelonQuantity = watermelonQuantity - watermelonReq
    watermelonTotal = watermelonPrice * watermelonReq
    if watermelonReq > watermelonQuantity :
        print("There are not enough kilos of watermelons")
        return 0
    else:
        print(f"Thanks for buying. You total price of watermelons are {watermelonTotal}")
    return watermelonTotal

def melon():
    melonPrice = 250
    melonQuantity = 25
    melonTotal = 0
    melonReq = int(input(f"There are {melonQuantity} kilograms of melon, each kilo cost {melonPrice} pkr."))
    melonQuantity = melonQuantity - melonReq
    melonTotal = melonPrice * melonReq
    if melonReq > melonQuantity :
        print("There are not enough kilos of melons")
        return 0
    else:
        print(f"Thanks for buying. You total price of melons are {melonTotal}")
    return melonTotal

def grapes():
    grapesPrice = 120
    grapesQuantity = 25
    grapesTotal = 0
    grapesReq = int(input(f"There are {grapesQuantity} dozens of grapes, each dozen cost {grapesPrice} pkr."))
    grapesQuantity = grapesQuantity - grapesReq
    grapesTotal = grapesPrice * grapesReq
    if grapesReq > grapesQuantity :
        print(f"There are not enough dozens of grapes")
        return 0
    else:
        print(f"Thanks for buying. You total price of grapes are {grapesTotal}")
        return grapesTotal


def fruits():
    buyFruit = input("Which fruit do you want to buy? ")
    if buyFruit == "watermelon":
        return watermelon()
    elif buyFruit == "apple":
        return apple()
    elif buyFruit == "melon":
        return melon()
    elif buyFruit == "grapes":
        return grapes()
    elif buyFruit == "banana":
        return banana()
    else:
        print(f"We have no fruit that name is {buyFruit}. retry. ")
        fruits()
    return 0

def more():
    morefruits = input("Do you want to buy more fruits? (yes/no): ")
    if morefruits == "yes":
        fruits()
    elif morefruits == "no":
        print("Goodbye")
    else:
        print(f"Please enter yes or no.")
        more()

def Total():
    bananaTotal = banana()
    watermelonTotal = watermelon()
    appleTotal = apple()
    grapesTotal = grapes()
    melonTotal = melon()
    GrandTotal = bananaTotal + watermelonTotal + appleTotal + grapesTotal + melonTotal
    return GrandTotal