from banana import banana
from banana import apple
from banana import watermelon
from banana import melon
from banana import grapes
from banana import more
from banana import fruits
from aisle1 import aisle1

print(f"Hello and welcome to RAS Store")
whichAisle = input("Which Aisle? ")
if whichAisle == "aisle1":
    aisle1()
    bananaTotal = banana()
    appleTotal = apple()
    watermelonTotal = watermelon()
    melonTotal = melon()
    grapesTotal = grapes()
    grandtotal = bananaTotal + appleTotal + watermelonTotal + melonTotal + grapesTotal
    print(f"Your grand total from Aisle No:1 is {grandtotal}")
else:
    print("Sorry that aisle don't exist!.")
    whichAisle