from aisle1 import aisle1
from banana import Total

# bananaTotal = banana()
# appleTotal = apple()
# watermelonTotal = watermelon()
# melonTotal = melon()
# grapesTotal = grapes()
print(f"Hello and welcome to RAS Store")
whichAisle = input("Which Aisle? ")
if whichAisle == "aisle1":
    GrandTotal = Total()
    print(f"Your grand total from Aisle No:1 is {GrandTotal}")
else:
    print("Sorry that aisle don't exist!.")
    whichAisle



