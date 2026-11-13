def toiletPaper():
    tioletPaperPrice = 200
    tioletPaperQuantity = 25
    tioletPaperTotal = 0
    tioletPaperReq= int(input(f"There are {tioletPaperQuantity} stes of tiolet Paper, each set cost {tioletPaperPrice} pkr. How much do you want: "))
    tioletPaperQuantity = tioletPaperQuantity - tioletPaperReq
    tioletPaperTotal = tioletPaperPrice * tioletPaperReq
    if tioletPaperReq > tioletPaperQuantity :
        print("There are not enough sets of tiolet Paper")
        return 0
    else:
        print(f"Thanks for buying. You total price of tioletPaper are {tioletPaperTotal}")
    return tioletPaperTotal

def facewash():
    facewashPrice = 800
    facewashQuantity = 25
    facewashTotal = 0
    facewashReq= int(input(f"There are {facewashQuantity} facewashes, each facewash cost {facewashPrice} pkr. How much do you want: "))
    facewashQuantity = facewashQuantity - facewashReq
    facewashTotal = facewashPrice * facewashReq
    if facewashReq > facewashQuantity :
        print("There are not enough facewashes")
        return 0
    else:
        print(f"Thanks for buying. You total price of facewash are {facewashTotal}")
    return facewashTotal

def soap():
    soapPrice = 100
    soapQuantity = 250
    soapTotal = 0
    soapReq= int(input(f"There are {soapQuantity} soap, each soap cost {soapPrice} pkr. How much do you want: "))
    soapQuantity = soapQuantity - soapReq
    soapTotal = soapPrice * soapReq
    if soapReq > soapQuantity :
        print("There are not enough soaps")
        return 0
    else:
        print(f"Thanks for buying. You total price of soap are {soapTotal}")
    return soapTotal

def shampoo():
    shampooPrice = 450
    shampooQuantity = 50
    shampooTotal = 0
    shampooReq= int(input(f"There are {shampooQuantity} shampoos, each facewash cost {shampooPrice} pkr. How much do you want: "))
    shampooQuantity = shampooQuantity - shampooReq
    shampooTotal = shampooPrice * shampooReq
    if shampooReq > shampooQuantity :
        print("There are not enough shampoos")
        return 0
    else:
        print(f"Thanks for buying. You total price of shampoo are {shampooTotal}")
    return shampooTotal

def paste():
    pastePrice = 150
    pasteQuantity = 50
    pasteTotal = 0
    pasteReq= int(input(f"There are {pasteQuantity} Tooth Pastes, each one cost {pastePrice} pkr. How much do you want: "))
    pasteQuantity = pasteQuantity - pasteReq
    pasteTotal = pastePrice * pasteReq
    if pasteReq > pasteQuantity :
        print("There are not enough Tooth Pastes")
        return 0
    else:
        print(f"Thanks for buying. You total price of Tooth paste are {pasteTotal}")
    return pasteTotal

def brush():
    brushPrice = 150
    brushQuantity = 150
    brushTotal = 0
    brushReq= int(input(f"There are {brushQuantity} shampoos, each one cost {brushPrice} pkr. How much do you want: "))
    brushQuantity = brushQuantity - brushReq
    brushTotal = brushPrice * brushReq
    if brushReq > brushQuantity :
        print("There are not enough Tooth paste")
        return 0
    else:
        print(f"Thanks for buying. You total price of Tooth brush are {brushTotal}")
    return brushTotal

def restroom():
    buyRestProduct = input(f"Which product you want to buy? ")
    if buyRestProduct.lower() == "toilet paper":
        return toiletPaper()
    elif buyRestProduct.lower() == "shampoo":
        return shampoo()
    elif buyRestProduct.lower() == "tooth paste":
        return paste()
    elif buyRestProduct.lower() == "tooth brush":
        return brush()
    elif buyRestProduct.lower() == "soap":
        return soap()
    elif buyRestProduct.lower() == "face wash":
        return facewash()
    else:
        print(f"Sorry ! We don't have {buyRestProduct} in our store")
        return restroom()

def restmore():
    morerest  = input(f"Do you want to buy more? ")
    if morerest.lower() == "yes":
        return restroom() + restmore()
    elif morerest.lower() == "no":
        print("Goodbye")
        return 0
    else:
        print(f"Please enter yes or no")
        return restmore()

def restroomTotal():
    soapTotal = soap()
    tioletpaperTotal = toiletPaper()
    facewashTotal = facewash()
    shampooTotal = shampoo()
    pasteTotal = paste()
    brushTotal = brush()
    restroomGrandtotal = soapTotal + tioletpaperTotal + facewashTotal + shampooTotal + pasteTotal + brushTotal
    return restroomGrandtotal