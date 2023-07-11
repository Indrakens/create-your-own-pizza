# PIZZA - TIME
A Python command line program. This application is a Python-based program to let users use their imagination and create their own pizza.
## [THE LIVE SITE]( https://pizzatime-35d0c564b83d.herokuapp.com/ )
## [REPOSITORY]( https://github.com/Indrakens/pizza-time )
# CONTENT TABLE
* ### [FLOWCHART]( https://github.com/Indrakens/pizza-time#flowchart-1 )
* ### [RUNNING PROGRAM]( https://github.com/Indrakens/pizza-time#running-program-1 )
* ### [TEHNOLOGY USED]( https://github.com/Indrakens/pizza-time#tehnology-used-1 )
* ### [TESTING]( https://github.com/Indrakens/pizza-time#testing-1 )
* ### [USER TESTS]( https://github.com/Indrakens/pizza-time#user-tests-1 )
* ### [PEP8]( https://github.com/Indrakens/pizza-time#pep8-ci-python-linter )
* ### [DEPLOYMENT]( https://github.com/Indrakens/pizza-time#deployment-1 )
* ### [CREDITS]( https://github.com/Indrakens/pizza-time#credits-1 )
* ### [BUGS]( https://github.com/Indrakens/pizza-time#bugs-1 )
* ### [RESOURCES]( https://github.com/Indrakens/pizza-time#resources-1 )
* ### [ACKNOWLEDGMENT]( https://github.com/Indrakens/pizza-time#acknowledgment-1 )
## FLOWCHART
To better understand the initial design and concept of the program.
![Pizza-Time (1)](https://github.com/Indrakens/pizza-time/assets/127971416/ac614b5a-9268-4f5e-b7e6-3f48e6899397)
## RUNNING PROGRAM
* When users open the program they are presented with a welcome message and name input.
![IMG_0856](https://github.com/Indrakens/pizza-time/assets/127971416/e1204e0d-6be1-4ec1-9827-b63ff9648812)
* After entering the name, the user is presented with a welcome message, with thr message "No pizza created yet!" and menu options.
![IMG_0867](https://github.com/Indrakens/pizza-time/assets/127971416/c661c6dd-3266-4906-b97e-5234fd3ddda5)
* When selecting C the user is presented with pizza size option.
![IMG_0860](https://github.com/Indrakens/pizza-time/assets/127971416/58baa939-7977-41df-a5c0-837f5ffd78fa)
* When selecting pizza size the user is presented with topping examples and has given option to type toppings or type e to stop a program.
![IMG_0861](https://github.com/Indrakens/pizza-time/assets/127971416/2cc25ba8-90ec-4225-9bf5-450a013033fc)
* When selecting O the user is presented with message Your Created Pizza and below will be able to see user created pizza.
![IMG_0862](https://github.com/Indrakens/pizza-time/assets/127971416/b3c6bcae-b77a-462a-b9f9-ee9cceb4a576)
* When selecting D the user is presented with message to enter the pizza number user would like to delete.
![IMG_0863](https://github.com/Indrakens/pizza-time/assets/127971416/03c37353-21ff-4826-b4a3-dba9f461363c)
* Selecting Q to end the program the user will be presented with thank you message.
![IMG_0864](https://github.com/Indrakens/pizza-time/assets/127971416/91ff9f61-bc00-4cfb-b6ed-21693f61c87d)
## TEHNOLOGY USED
### Python
Used to create the application.
### Heroku
Used to deploy and host the application.
### Github
Used to store the code.
### Gitpod
IDE used to creating the application.
### Git
Used for version control.
## TESTING
### Testing Steps:
|                    TEST                                                              | RESULT |
|---------|-----------|
| On the run program the welcome message appears                                       |  PASS  |
| After the welcome message user was asked to enter a name before continuing           |  PASS  |
| After the text enter your name before continuing, user prompted for name             |  PASS  |
| Once the name is input the welcome message and menu option presents                  |  PASS  |
| Selecting C to create                                                                |  PASS  |
| After selecting C pizza size options presents                                        |  PASS  |
| After selecting pizza size, topping examples ,and type toppings or e to stop presents|  PASS  |
| After typing topping the type toppings or e to stop option presents                  |  PASS  |
| After typing e to stop, shows created pizza ,and menu option presents                |  PASS  |
| Selecting D user asked to enter the pizza number to delete                           |  PASS  |
| After selectin pizza to delete the menu option presents                              |  PASS  |
| Selectin O shows created pizza and the menu option presents                          |  PASS  |
| Selecting Q end of the program and than you message appears                          |  PASS  |

## User Tests: 
The following tests are on error handling true out the project.
Enter Your Name Field.                                     
|            TEST                                   | RESULT |
|---------|---------|
| The user enters the number                        |  PASS  |
| The user tried to enter the name with a number    |  PASS  |
| The user enters an empty string                   |  PASS  |
| The user tried to enter a name with a space in it |  PASS  |
| The user enters two or more names                 |  PASS  |
#### The users can only enter one name to continue.
Choose one of the options in the Main Menu Field.                               
|            TEST                                             | RESULT |
|----------|----------|
| The user enters the full name of one of the options         |  PASS  |
| The user enters the number                                  |  PASS  |
| The user enters the option letter and number                |  PASS  |
| The user enters an empty string                             |  PASS  |
| The user enters more than one letter                        |  PASS  |
| The user enters a letter what is not included in the options|  PASS  |
#### The users can only enter the letter that shows in the main menu options.
Choose one of the options in the Pizza Size Field.
|           TEST                                              | RESULT |
|-------|--------|
| The user enters the number                                  |  PASS  |
| The user enters any name                                    |  PASS  |
| The user enters a letter what is not included in the options|  PASS  |
| The user enters an empty string                             |  PASS  |
| The user enters more than one letter                        |  PASS  |
#### The users can only enter the letter that shows in the pizza size options.
Enter topping or e in the - "Please type toppings or e to stop" Field.
|      TEST                                 | RESULT |
|--------|----------|
| The user enters the number                |  PASS  |
| The user enters an invalid topping        |  PASS  |
| The user enters an empty string           |  PASS  |
| The user enters an invalid letter to stop |  PASS  |
#### The users can only enter the toppings provided in topping examples or enter (e) to stop.
Deleting pizza in Enter pizza number to delete Field.
|    TEST                          | RESULT |
|--------|---------|
| The user enters the letter       |  PASS  |
| The user enters name             |  PASS  |
| The user enters an empty string  |  PASS  |
| The user enters the wrong number |  PASS  |   
#### The users can only enter the pizza number they would like to delete. If pizza is not created yet they will see an error message "Entered pizza doesn't exist!".
Opening pizza in "Your Created Piza!" Field.
|     TEST                              | RESULT |
|------|------|
| The user hasn't yet created any pizza |  PASS  |
#### The user can see created pizza only if the pizza has been created.
## PEP8 CI Python Linter
![IMG_0854](https://github.com/Indrakens/pizza-time/assets/127971416/ec1ef63a-923b-49e9-8535-ef2adcae0d22)
## DEPLOYMENT
* Navigate to heroku.com and log in.
* Click "new" and create a new App.
* Give the application a name and then choose your region and Click "Create app".
* After you create App click on Settings to adjust the settings.
* Click on the "Config Vars" button.
* Supply a KEY of PORT and it's VALUE of 8000. Then click on the "add" button.
* If you have creds.jason file in your project.
* Supply a KEY of CREDS and its VALUE of copied entire creds. jason file.
* Click on Buildpack to install future dependencies that we need outside of the requirements file.
* Select Python first and save.
* Select nodejs and save.
* After Settings go to the Deploy section.
* To connect with github select github and confirm.
* Search for your repository, type your repository name, select it, and click to connect.
* You can choose to either deploy using automatic deploys which means Heroku will rebuild the app every time you push your changes.
* For this option choose the branch to deploy and click enable automatic deploys.
* Manual deployment deploys the current state of a branch. 
* Click to deploy branch.
* Now you can click on the open App button to view our application.
## CREDITS
* For having color and style for texts in the program installed simple-colors [PYPI]( https://pypi.org/project/simple-colors/). To install simple colors in the terminal you have to type pip install simple-colors and press enter.
## BUGS
To display an error message for pizza size. Removed [0].
* Before fixing the issue the code was:

'''

    while True:
        size = input("(S) (M) (L): ")[
            0].upper()
        if size.upper() not in ("S", "M", "L"):
            print(simple_colors.red("Please enter valid option!\n", 'italic'))
        else:
            break

'''

* Fixed code entering topping or e to stop:
   * Before:

    '''

        while True:
        topping = input(yellow(
            "Please type a toppings or (e) to stop: ", ['italic', 'bright']))
        if topping == "e":
            break

    ''' 

    * After:

    '''

        while True:
        topping = input(yellow(
            "Please type a toppings or (e) to stop: ", ['italic', 'bright']))
        if topping.lower() not in ("cheese", "mushrooms", "pineapple",
                                   "tomato", "chicken", "olives", "onion",
                                   "chilli", "bacon", "peppers",
                                   "sausage", "pepperoni", "e"):
            print(red("Please enter valid option!", ['italic', 'bright']))
            break
        elif topping == "e":
            break

    '''  

Deleting pizzas- when you enter number 1 it was deleting number 2. To fix this- add to index_to_delete -1. 
* Before fixing the issue the code was:

''' 

    if (index_to_delete > 0 and index_to_delete <= len(pizzas)):
                del pizzas[index_to_delete]

'''               

## RESOURCES
* w3schools - used to reference Python structure
* Youtube - use it every day while coding to help understand different outlooks in coding.
## ACKNOWLEDGMENT 
* Graeme Taylor - my mentor who provided me with great feedback and guidance at the inception of this project.
* Alan Bushell - our teacher, always a great mentor during stand-up. And who helped insure me to get true this project.