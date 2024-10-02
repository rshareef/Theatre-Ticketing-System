# IN0005 FINAL PROJECT: MILESTONE 2

### MAIN PROGRAM TO RUN

### IMPORTS
# import functions used in this file from user defined modules.
from common_module import initialiseFiles, quitProgram
from admin_module import adminOptionMenu
from normal_user_module import normalUserProgramEntry


### MAIN PROGRAM
## 
# check if this is the first time the program has ever been run (i.e. text files "bookings.txt" and/or "usernames.txt" do not exist).
# alternatively, the program may have been run, but the user could have accidentally deleted the relevant text files so, incase, we check that BOTH files exist.
# if either one does not exist, I have chosen to initialise both files again (as the contents of both are connected), using the function 'initialiseFiles' [imported from 'common_module'].
initialiseFiles()


## 
# program title.
print("--------------------------\nTheatre Ticketing System\n--------------------------", end="")


## 
# users will be asked whether they are an admin or not.
# loop until a valid input is provided.
while True:
    # ask the user to provide input.
    userType = input('''
Are you an admin? (Y/N)
Enter the letter that corresponds with your choice, e.g. "N":
    Y - Admin
    N - Not an Admin
(or Q - Quit program)
>>>''')

    # NOTE: I have applied both '.upper()' and '.strip()' functions to the user input 'userType' to accept the user's input even if they have used lowercase 'y/n' instead, or have any leading/ending whitespaces in their input, and have stored this in the variable 'modifiedInput'.
    modifiedInput = (userType.upper()).strip()
    # all of the functions invoked as a result of a valid input will eventually quit the program for the user when they decide to quit at whatever stage, using the function 'quitProgram'.
    # if the user is an ADMIN user:
    if modifiedInput == "Y":
        # output a message for the user.
        print("\nAdmin entry successful.")
        # call the function 'adminOptionMenu' [imported from 'admin_module'], to show the admin main menu.
        adminOptionMenu()
    # if the user is not an admin user, they are a NORMAL user, so:
    elif modifiedInput == "N":
        # call the function 'normalUserProgramEntry' [imported from 'normal_user_module'], to allow the user to register/log-in.
        normalUserProgramEntry()
        # if the user has exited the 'normalUserProgramEntry' function, this while loop will allow them to re-enter their user type.
    # give the user a chance to exit the program at this stage if they would like to by calling the 'quitProgram' function [imported from 'common_module'].
    elif modifiedInput == "Q":
        quitProgram()
    # otherwise if the user input is invalid, output a statement for the user before moving to the next while loop iteration.
    else:
        print(f"'{userType}' is not an option you may choose.\nPlease try again.")