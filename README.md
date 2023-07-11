# PIZZA - TIME
A Python command line program. This application is a Python-based program to let users use their imagination and create their own pizza.
## THE LIVE SITE
## REPOSITORY
# CONTENT TABLE
# FLOWCHART
To better understand the initial design and concept of the program.
![Pizza-Time](https://github.com/Indrakens/pizza-time/assets/127971416/070fb8d2-48c4-4ce9-838c-9ef056d3d1cf)
# RUNNING PROGRAM
When users open the program they are presented with a welcome message and name input.
![3D793E15-E72F-415D-A73A-248C57ECC67B](https://github.com/Indrakens/pizza-time/assets/127971416/7e2ab970-21e1-4697-8d64-d6f2fe534198)
The user is presented with a welcome message and menu options.
![74C75FC9-D950-4356-AF21-9E2B3AF3D12A](https://github.com/Indrakens/pizza-time/assets/127971416/c9b5c3b4-4bbb-4650-a0f8-b3484c7bc1ce)
When selecting C the user is presented with pizza size option.
![0ACDEEBB-0EA2-480C-AE3A-A25DE0807171](https://github.com/Indrakens/pizza-time/assets/127971416/eb882299-00aa-4721-a4b1-3c7816eaad7e)
When selecting pizza size the user is presented with topping examples and has given option to type toppings or type e to stop a program.
![2B1BC813-E273-441C-B58F-859BB15BDAD8](https://github.com/Indrakens/pizza-time/assets/127971416/5480c279-a92c-4fe5-a624-cb36e5c2b1d5)
When selecting O the user is presented with message Your Created Pizza and below will be able to see user created pizza.
![EADE79DC-8275-4C17-956A-E82CB7C8BE01](https://github.com/Indrakens/pizza-time/assets/127971416/d2790e98-92ed-445e-8d67-5d11ac07900e)
When selecting D the user is presented with message to enter the pizza number user would like to delete.
![6A6FE4A3-F8DA-49EE-B7A1-E847B999E85F](https://github.com/Indrakens/pizza-time/assets/127971416/bb1bbe02-255e-4e0d-a63d-0347d0193053)
Selecting Q to end the program the user will be presented with thank you message.
![0768D94B-88DA-4C28-8A5C-D4DFE8C48A3B](https://github.com/Indrakens/pizza-time/assets/127971416/f6d8742a-6b1b-45c8-9b19-5d93b06c3b4b)
# TEHNOLOGY USED
## Python
Used to create the application.
## Heroku
Used to deploy and host the application.
## Github
Used to store the code.
## Gitpod
IDE used to creating the application.
## Git
Used for version control.
# TESTING
## Testing Steps:
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
| Enter Your Name Field.                                     |
|-----------|-------|
|            TEST                                   | RESULT |
|---------|---------|
| The user enters the number                        |  PASS  |
| The user tried to enter the name with a number    |  PASS  |
| The user enters an empty string                   |  PASS  |
| The user tried to enter a name with a space in it |  PASS  |
| The user enters two or more names                 |  PASS  |
The users can only enter one name to continue.
| Choose one of the options in the Main Menu Field.                    |             
|-------------|--------|
|            TEST                                             | RESULT |
|----------|----------|
| The user enters the full name of one of the options         |  PASS  |
| The user enters the number                                  |  PASS  |
| The user enters the option letter and number                |  PASS  |
| The user enters an empty string                             |  PASS  |
| The user enters more than one letter                        |  PASS  |
| The user enters a letter what is not included in the options|  PASS  |
The users can only enter the letter that shows in the main menu options.
# PEP8 CI Python Linter
![9EAA5702-F173-4096-AE3F-E6737C43562B](https://github.com/Indrakens/pizza-time/assets/127971416/76e925d8-b06d-42dd-a33e-c82e29412f66)
# DEPLOYMENT
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