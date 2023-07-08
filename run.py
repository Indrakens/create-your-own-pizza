from simple_colors import *


def program_start():
    """
    Start of the program.
    """
    print(yellow(
        "-----------------------------------------", ['bright', 'bold']))
    print(yellow(
        "        WELCOME TO PIZZA-TIME!         ", ['bold', 'bright']))
    print(yellow("        Create your own pizza.      ", 'bright'))
    print(yellow(
        "-----------------------------------------", ['bright', 'bold']))


def get_ueser_name():
    """
    Get the name of the user.
    """
    print(yellow(
        "Please enter your name before continuing.", ['italic', 'bright']))
    while True:
        name = input(cyan(
            "ENTER YOUR NAME:\n", ['bold', 'italic']))
        if name.isalpha():
            print(yellow("Hello," + name +
                  "! Enjoy creating your own pizza!\n", ['italic', 'bright']))
            return name
        else:
            print(red(
                "Invalid name, please try again!\n", ['italic', 'bright']))


def display_pizzas(pizzas):
    """
    Displays the size and toppings of the pizza.
    """
    if len(pizzas) == 0:
        print(red("No pizza created yet!", ['italic', 'bright']))
    else:
        index = 1
        for pizza in pizzas:
            print(f"{index}: {pizza[0]} pizza with {', '.join(pizza[1])}.")
            index += 1


def get_user_choice():
    """
    Get the user to pick one of the options.
    """
    print(yellow("Please choose one of the options!", ['italic', 'bright']))
    choice = input(cyan(
        "(C)reate, (D)elete, (O)pen created pizza, (Q)uit:\n",
        ['bold', 'italic'])).upper()

    return choice


def add_pizza(pizzas):
    """
    Get the user to choose and enter pizza size.
    After entering size users can type toppings.
    """
    print(yellow(
        "Please enter pizza size.", ['italic', 'bright']))
    while True:
        size = input(cyan(
            "(S) (M) (L):\n", ['italic', 'bold'])).upper()
        if size.upper() not in ("S", "M", "L"):
            print(red("Please enter valid option!\n", ['italic', 'bright']))
        else:
            break

    print(cyan("TOPPING EXAMPLES...", 'italic'))
    examples = ["-cheese", "-pepperoni", "-mushrooms", "-onion", "-sausage",
                "-olives", "-peppers", "-pineapple", "-chicken", "-bacon"]
    for example in examples:
        print(example, end="")
        print("\b\b", end="")
        print("")

    toppings = []
    while True:
        topping = input(yellow(
            "Please type a toppings or (e) to stop:\n", ['italic', 'bright']))

        if topping == "e":
            break

        toppings.append(topping)

    pizza = (size, toppings)
    pizzas.append(pizza)


def delete_pizza(pizzas):
    """
    Users can delete a pizza by entering the index number of the pizza created.
    """
    while True:
        try:
            index_to_delete = int(
                input(yellow(
                    "Enter pizza number to delete: ", ['italic', 'bright'])))

            if (index_to_delete > 0 and index_to_delete <= len(pizzas)):
                del pizzas[index_to_delete-1]
            else:
                print(red(
                    "Entered pizza don't exist.", ['italic', 'bright']))

        except ValueError:
            print(red("Invalid number!", ['italic', 'bright']))
        break


def open_created_pizza(pizzas):
    """
    Displays what pizza is created by the user.
    Or displays the text "NO PIZZA CREATED YET!"
    """
    print(cyan(
        "---YOUR CREATED PIZZA---", 'italic'))


def program_end():
    """
    End of the program.
    """
    print(yellow(
        "----------------------------------------------", ['bright', 'bold']))
    print(yellow(
        "       THANK YOU FOR USING PIZZA-TIME!", ['bright', 'bold']))


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
            print(red("Please enter a valid option!", ['italic', 'bright']))

    program_end()


main()
