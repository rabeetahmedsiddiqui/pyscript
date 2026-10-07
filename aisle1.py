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
        return fruits()
    elif want == "no":
        print("Goodbye")
        return 0
    else:
        print("Please enter yes or no.")