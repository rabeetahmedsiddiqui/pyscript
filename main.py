from aisle1 import aisle1
from banana import fruitTotal
from banana import more
from aisle2 import aisle2
from restroom import restroomTotal

def main():
    whichAisle = input("Which Aisle? ")
    if whichAisle == "aisle 1":
        fruitGrandTotal = aisle1()
        print(f"Your grand total from Aisle No:1 is {fruitGrandTotal}")
        return fruitGrandTotal, main()
    elif whichAisle == "aisle 2":
        restroomGrandtotal = aisle2()
        print(f"Your grand total from Aisle No:2 is {restroomGrandtotal}")
        return restroomGrandtotal, main()
    else:
        print("Sorry that aisle don't exist!.")
        whichAisle

print(f"Hello and welcome to RAS Store")
main()