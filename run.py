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


def add_pizza(pizzas):
    """
    Get the user to choose and enter pizza size.
    After entering size users can type toppings.
    """
    print("Please enter pizza size you would like to create.")
    size = input("SIZES (S) (M) (L): ")[
        0].upper()
    print()
    print("EXAMPLES...")
    print("--cheese")
    print("--pepperoni")
    print("--mushrooms")
    print("--onions")
    print("--sausage")
    print("--olives")
    print("--peppers")
    print("--pineapple")
    print("--tomato")
    print("--chicken")
    print("--bacon")

    toppings = []
    while True:
        topping = input(
            "Please type a toppings of your choice, or type end to stop: ")

        if topping == "end":
            break
        toppings.append(topping)

    pizza = (size, toppings)
    pizzas.append(pizza)               


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
    pizzas = []

    while True:
        choice = get_user_choice()
        if choice == "C":
            add_pizza(pizzas)
        elif choice == "Q":
            break
        else:
            print("Please enter a valid option!")
    

main()