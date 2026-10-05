def signIn():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    Email = input("Enter your E-mail: ")
    Password = input("Enter your Password: ")
    if age < 18:
        print("your account may restrict some content")
    else:
        print("Your account is an adult account")
    return Email, Password

def Login(Email, Password):
    email = input("Enter your E-mail: ")
    password = input("Enter your Password: ")
    if email == Email and password == Password:
        print("You are logged in")
    else:
        print("Invalid E-mail or Password")



confirm = input("Do you want to create an account? (yes/no): ")

if confirm == "no":
    print("You have chosen not to create an account.")
if confirm != "yes" and confirm != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")

if confirm == "yes":
    Email, Password = signIn()
    logIn = input("Now that your account is created, do you want to log in? (yes/no): ")
    if logIn.lower() == "yes":
        Login(Email, Password)
