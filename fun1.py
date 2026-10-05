def signIn ():
    name = input("Enter Your name: ")
    print("Hello, welcome ", name)
    Email = input("Enter your Email: ")
    if "@gmail.com" in Email:
        age = int(input("Enter Your age "))
    else:
        print("Email must contain at least '@gmail.com' ")
        signIn()
    Password = input("Enter the password: ")
    if age < 18:
        print(f"Sorry {name} hence your age is just {age} there may be some restricted content")
    else:
        print("You have an adult account")
    return Email, Password

def logIn(Email, Password):
    email = input("Enter your E-Mail ")
    password = input("Enter your Password ")
    if email == Email and password == Password:
        print("Log In successful!")
    else:
        print("Invalid email or password!")
        logIn(Email, Password)

def main(Email, Password):
    req = input("Now You can Log In (yes/no): ")
    if req.lower() == "yes":
        logIn(Email, Password)
    elif req.lower() == "no":
        print("Ok you choose not to Log In")
    else:
        print("Please enter yes or no")
        main()

def loop():
    signinConfirm = input("Do you want to sign In (yes/no) ")
    if signinConfirm.lower() == "yes":
        Email, Password = signIn()
        req = main(Email, Password)

    elif signinConfirm.lower() == "no":
        print("You chose not to Sign IN")
    else:
        print("please enter yes or no")

loop()