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


def get_user_choice():
    """
    Get the user to pick one of the options.
    """
    print("Please choose one of the options!")
    choice = input("(C)reate, (D)elete, (O)pen created pizza, (Q)uit: ")[
        0].upper()
    print()

    return choice            


def program_end():
    """
    End of the program.
    """
    print("THANK YOU FOR USING PIZZA CREATOR!")                


def main():
    """
    Runs all functions.
    """
    header()
    name()
    program_end()
    choice = get_user_choice()


main()