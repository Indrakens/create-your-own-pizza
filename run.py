import simple_colors


def program_start():
    """
    Start of the program.
    """
    print(simple_colors.red(
        "-----------------------------------------", ['bright', 'bold']))
    print(simple_colors.red(
        "        WELCOME TO PIZZA-TIME!         ", ['bold', 'bright']))
    print(simple_colors.red("        Create your own pizza.      ", 'bright'))
    print(simple_colors.red(
        "-----------------------------------------", ['bright', 'bold']))


def get_ueser_name():
    """
    Get the name of the user.
    """
    print(simple_colors.yellow(
        "Please enter your name before continuing.", 'italic'))
    while True:
        name = input(simple_colors.green(
            "ENTER YOUR NAME: ", ['bold', 'italic']))
        if name.isalpha():
            print(simple_colors.yellow("Hello," + name +
                  "! Enjoy creating your own pizza!\n", 'italic'))
            return name
        else:
            print(simple_colors.red(
                "Invalid name, please try again!\n", 'italic'))


def display_pizzas(pizzas):
    """
    Displays the size and toppings of the pizza.
    """
    if len(pizzas) == 0:
        print(simple_colors.red("No pizza created yet!", 'italic'))
    else:
        index = 1
        for pizza in pizzas:
            print(f"{index}: {pizza[0]} pizza with {', '.join(pizza[1])}.")
            index += 1


def get_user_choice():
    """
    Get the user to pick one of the options.
    """
    print(simple_colors.yellow("Please choose one of the options!", 'italic'))
    choice = input(simple_colors.green(
        "(C)reate, (D)elete, (O)pen created pizza, (Q)uit: ",
        ['bright', 'bold', 'italic'])).upper()

    return choice


def add_pizza(pizzas):
    """
    Get the user to choose and enter pizza size.
    After entering size users can type toppings.
    """
    print(simple_colors.yellow(
        "Please enter pizza size you would like to create.", 'italic'))
    while True:
        size = input(simple_colors.green(
            "(S) (M) (L): ", ['bright', 'bold'])).upper()
        if size.upper() not in ("S", "M", "L"):
            print(simple_colors.red("Please enter valid option!\n", 'italic'))
        else:
            break

    print(simple_colors.green("TOPPING EXAMPLES...", 'italic'))
    examples = ["-cheese", "-pepperoni", "-mushrooms", "-onion", "-sausage",
                "-olives", "-peppers", "-pineapple", "-chicken", "-bacon"]
    for example in examples:
        print(example, end="")
        print("\b\b", end="")
        print("")

    toppings = []
    while True:
        topping = input(simple_colors.yellow(
            "Please type a toppings or type end to stop: ", 'italic'))

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
        input(simple_colors.yellow(
            "Enter index number of pizza you'd like to delete: ", 'italic')))
    if (index_to_delete > 0 and index_to_delete <= len(pizzas)):
        del pizzas[index_to_delete-1]
    else:
        print(simple_colors.red(
            "The pizza you entered does not exist.", 'italic'))


def open_created_pizza(pizzas):
    """
    Displays what pizza is created by the user.
    Or displays the text "NO PIZZA CREATED YET!"
    """
    print(simple_colors.magenta(
        "---YOUR CREATED PIZZA---", ['bright', 'italic']))


def program_end():
    """
    End of the program.
    """
    print(simple_colors.red(
        "----------------------------------------------", ['bright', 'bold']))
    print(simple_colors.red(
        "       THANK YOU FOR USING PIZZA-TIME!", ['bright', 'bold']))
    print(simple_colors.red(
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
            print("Please enter a valid option!")

    program_end()


main()
