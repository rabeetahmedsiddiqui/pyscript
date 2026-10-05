from banana import banana
from banana import apple
from banana import watermelon
from banana import melon
from banana import grapes
from banana import more
from banana import fruits

def aisle1():
    print(f"Hello, This is aisle no:1 (for fruits)")
    print(f"We have: ")
    print("         Bananas")
    print("         Apples")
    print("         Watermelons")
    print("         melons")
    print("         Grapes")
    want = input(f"Do you want to buy fruits: (yes/no) ")
    if want == "yes":
        fruits()
    elif want == "no":
        print("Goodbye")
    else:
        print("Please enter yes or no.")
        want
