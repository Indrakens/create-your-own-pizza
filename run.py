def header():
    """
    Start of the program.
    """
    print("WELCOME TO CREATE YOUR OWN PIZZA!\n")


def name():
    """
    Get the name of the user.
    """
    print("Please enter your name before continuing.")
    while True:
        name = input("ENTER YOUR NAME: ")
        if name.isalpha():
            print("Hello," + name + "! Enjoy creating your own pizza!\n")
            return name
        else:
            print("Invalid name, please try again!\n")    


def main():
    """
    Runs all functions.
    """
    header()
    name()

main()