from simple_colors import *


def program_start():
    """
    Start of the program.
    """
    print(red(
        "-----------------------------------------", ['bright', 'bold']))
    print(red(
        "        WELCOME TO PIZZA-TIME!         ", ['bold', 'bright']))
    print(red("        Create your own pizza.      ", 'bright'))
    print(red(
        "-----------------------------------------", ['bright', 'bold']))


def get_ueser_name():
    """
    Get the name of the user.
    """
    print(yellow(
        "Please enter your name before continuing.", 'italic'))
    while True:
        name = input(green(
            "ENTER YOUR NAME:\n", ['bold', 'italic']))
        if name.isalpha():
            print(yellow("Hello," + name +
                  "! Enjoy creating your own pizza!\n", 'italic'))
            return name
        else:
            print(red(
                "Invalid name, please try again!\n", 'italic'))


def display_pizzas(pizzas):
    """
    Displays the size and toppings of the pizza.
    """
    if len(pizzas) == 0:
        print(red("No pizza created yet!", 'italic'))
    else:
        index = 1
        for pizza in pizzas:
            print(f"{index}: {pizza[0]} pizza with {', '.join(pizza[1])}.")
            index += 1


def get_user_choice():
    """
    Get the user to pick one of the options.
    """
    print(yellow("Please choose one of the options!", 'italic'))
    choice = input(green(
        "(C)reate, (D)elete, (O)pen created pizza, (Q)uit:\n",
        ['bright', 'bold', 'italic'])).upper()

    return choice


def add_pizza(pizzas):
    """
    Get the user to choose and enter pizza size.
    After entering size users can type toppings.
    """
    print(yellow(
        "Please enter pizza size you would like to create.", 'italic'))
    while True:
        size = input(green(
            "(S) (M) (L):\n", ['bright', 'bold'])).upper()
        if size.upper() not in ("S", "M", "L"):
            print(red("Please enter valid option!\n", 'italic'))
        else:
            break

    print(green("TOPPING EXAMPLES...", 'italic'))
    examples = ["-cheese", "-pepperoni", "-mushrooms", "-onion", "-sausage",
                "-olives", "-peppers", "-pineapple", "-chicken", "-bacon"]
    for example in examples:
        print(example, end="")
        print("\b\b", end="")
        print("")

    toppings = []
    while True:
        topping = input(yellow(
            "Please type a toppings or type (e)nd to stop:\n", 'italic'))

        if topping == "e":
            break
        toppings.append(topping)

    pizza = (size, toppings)
    pizzas.append(pizza)


def delete_pizza(pizzas):
    """
    Users can delete a pizza by entering the index number of the pizza created.
    """
    index_to_delete = int(
        input(yellow(
            "Enter index number of pizza you'd like to delete: ", 'italic')))
    if (index_to_delete > 0 and index_to_delete <= len(pizzas)):
        del pizzas[index_to_delete-1]
    else:
        print(red(
            "The pizza you entered does not exist.", 'italic'))


def open_created_pizza(pizzas):
    """
    Displays what pizza is created by the user.
    Or displays the text "NO PIZZA CREATED YET!"
    """
    print(magenta(
        "---YOUR CREATED PIZZA---", ['bright', 'italic']))


def program_end():
    """
    End of the program.
    """
    print(red(
        "----------------------------------------------", ['bright', 'bold']))
    print(red(
        "       THANK YOU FOR USING PIZZA-TIME!", ['bright', 'bold']))
    print(red(
        "       -------------------------------         ", ['bright', 'bold']))


def main():
    """
    Runs all functions.
    """
    program_start()
    get_ueser_name()
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
            print(red("Please enter a valid option!", 'italic'))

    program_end()


main()
