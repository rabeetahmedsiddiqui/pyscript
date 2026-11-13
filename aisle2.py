from restroom import restroom
from restroom import restmore
def aisle2():
    print(f"Hello, This is aisle no:1 (for Rest room Products)")
    print(f"We have: ")
    print("         Toilet Paper")
    print("         shampoo")
    print("         Face Wash")
    print("         Soap")
    print("         Tooth Brush")
    print("         Tooth Paste")
    want = input(f"Do you want to buy rest room products: (yes/no) ")
    if want == "yes":
        return restroom() + restmore()
    elif want == "no":
        print("Goodbye")
        return 0
    else:
        print("Please enter yes or no.")