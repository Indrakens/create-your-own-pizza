def header():
    """
    Start of the program.
    """
    print("--------------------------")
    print("WELCOME TO PIZZA-TIME!")
    print("--------------------------")
    print("Create your own pizza!\n")


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


def display_pizzas(pizzas):
    """
    Displays the size and toppings of the pizza.
    """
    if len(pizzas) == 0:
        print("NO PIZZA CREATED YET!")
        print("---------------------")
    else:
        index = 1
        for pizza in pizzas:
            print(f"{index}: {pizza[0]} pizza with {', '.join(pizza[1])}.")
            index += 1


def get_user_choice():
    """
    Get the user to pick one of the options.
    """
    print("Please choose one of the options!")
    print("---------------------------------------------------")
    choice = input("(C)reate, (D)elete, (O)pen created pizza, (Q)uit: ")[
        0].upper()
    print("---------------------------------------------------")
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
    print("TOPPING EXAMPLES...")
    examples = ["-cheese", "-pepperoni", "-mushrooms", "-onion", "-sausage",
                "-olives", "-peppers", "-pineapple", "-chicken", "-tomato", "-bacon"]
    for example in examples:
        print(example, end="")
        print("\b\b", end="")
        print("")

    toppings = []
    while True:
        topping = input(
            "Please type a toppings of your choice, or type end to stop: ")

        if topping == "end":
            break
        toppings.append(topping)

    pizza = (size, toppings)
    pizzas.append(pizza)


def delete_pizza(pizzas):
    """
    Users can delete a pizza by entering the index number of the pizza created.
    """
    index_to_delete = int(
        input("Please enter index number of pizza you'd like to delete: "))
    if (index_to_delete > 0 and index_to_delete <= len(pizzas)):
        del pizzas[index_to_delete-1]
    else:
        print("The pizza you entered does not exist.")


def open_created_pizza(pizzas):
    """
    Displays what pizza is created by the user.
    Or displays the text "NO PIZZA CREATED YET!"
    """
    print("---YOUR CREATED PIZZA---")


def program_end():
    """
    End of the program.
    """
    print("THANK YOU FOR USING PIZZA-TIME!")


def main():
    """
    Runs all functions.
    """
    header()
    name()
    pizzas = []

    while True:
        display_pizzas(pizzas)
        choice = get_user_choice()
        if choice == "C":
            add_pizza(pizzas)
        elif choice == "D":
            delete_pizza(pizzas)
        elif choice == "O":
            open_created_pizza(pizzas)
        elif choice == "Q":
            break
        else:
            print("Please enter a valid option!")

    program_end()


main()
