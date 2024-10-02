# IN0005 FINAL PROJECT: MILESTONE 2

# ADMIN USER MODULE (i.e. functions that are used by only Admin Users).

### IMPORTS
# functions from 'common_module' are referenced within this module, so I have imported it with a shorthand to make it clear which functions have been imported into this module.
import common_module as cm

### FUNCTIONS
# FUNCTION PURPOSE: To show the admin a layout of the theatre where all the bought tickets are marked with symbol x.
def viewTicketStatus():
    # display current booking status for the theatre (the already booked seats are marked with the symbol x). ['printTheatre' has been imported from 'common_module'].
    cm.printTheatre("","x")
    # ask the user to press enter to return to the main menu. I have included this here to give the user time to view the ticket status as long as they would like before they return to the main menu.
    # (since Milestone 1: 'press any key' has been changed to 'press enter' for simplicity as the user must press enter in the console anyway for input to be accepted).
    input("\nPress enter to return to the main menu.")
    # the user will be returned to the main menu automatically, once the function has completed execution.


# FUNCTION PURPOSE: To cancel all booked tickets in the theatre.
def reset():
    # check if the theatre is already empty (i.e. does not need to be reset).
    # flag 'continueReset' to determine whether to proceed to reset or exit the function.
    continueReset = True
    # load the theatre bookings 2D list from "bookings.txt" by calling  the function 'loadData' [imported from 'common_module'] and assign the return value to the variable 'data'.
    data = cm.loadData ("bookings.txt")
    # initialise variable to keep count of the running total of empty seats in the theatre.
    emptySeats = 0
    # check each seat in the theatre.
    for seat in data:
        # if the seat has not been booked by anyone (i.e. it is empty), increment the empty seat counter by 1.
        if seat[0] == "":
            emptySeats = emptySeats + 1
    # if the final total number of empty seats in the theatre is 98 (i.e. every single seat is empty):
    if emptySeats == 98:
        # output a message to the user that the theatre has already been reset.
        print("\nTheatre already reset.")
        # and do not start the reset process.
        continueReset = False
    
    # if there are any booked seats in the theatre, we may start the potential reset process.
    if continueReset == True:
        # display current booking status for the theatre (the already booked seats are marked with the symbol x). ['printTheatre' has been imported from 'common_module'].
        cm.printTheatre("","x")
        
        # establish a while loop.
        while True:
            # ask the admin to confirm that they want to reset the theatre bookings (so that all booked tickets are cancelled).
            confirm = input('''
Are you sure you want to reset (cancel all booked tickets in the theatre)? (Y/N)
Enter the letter that corresponds with your choice, e.g. "N":
    Y - Yes
    N - No
>>>''')
            # NOTE: I have applied both '.upper()' and '.strip()' functions to the user input 'confirm' to accept the user's input even if they have used lowercase 'y/n' instead, or have any leading/ending whitespaces in their input, and have stored this in the variable 'modifiedInput'.
            modifiedInput = (confirm.upper()).strip()
            # if the user confirms the reset:
            if modifiedInput == "Y":
                # re-initialise the theatre by calling the function 'initialiseTheatre()' [imported from 'common_module'].
                cm.initialiseTheatre()
                # confirm to the user that the theatre has been reset.
                print("Reset Successful.")
                # exit the while loop.
                break
            # if the user does NOT confirm the reset:
            elif modifiedInput == "N":
                # output a message to the user stating that the reset has been cancelled.
                print("Reset cancelled.")
                # exit the while loop.
                break
            # if the user enters anything else (i.e. an invalid input):
            else:
                # output a message to the user stating their input is not an option.
                print(f"'{confirm}' is not an option you may choose.\nPlease try again.")
                # continue to the next iteration of the while loop.
    # the user will be returned to the main menu automatically, once the function has completed execution.


# FUNCTION PURPOSE: To display the option menu for an admin user and run the function corresponding to their input choice.
def adminOptionMenu():  
    # establish a while loop. loop until the user chooses to quit (option 4).
    while True:
        # print out an option menu and ask the user to enter a number corresponding to their functionality choice.
        option = input('''
Main Menu
Please enter a number from 1-4 that matches your option choice:
1. View Ticketing Status
2. Cancel ticket
3. Reset
4. Quit
>>>''')
        # NOTE: I have applied the '.strip()' function to the user input 'option' to accept the user's input even if they have any leading/ending whitespaces in their entry.
        option = option.strip()
        
        # if the user has chosen a valid option (number from 1-4), invoke the correct function for the option selected.
        if option == "1":
            viewTicketStatus()
        elif option == "2":
            cm.cancelTicket()
        elif option == "3":
            reset()
        elif option == "4":
            cm.quitProgram()
        
        # if the user enters anything else (i.e. an invalid input):
        else:
            # output a message to the user stating their input is not an option.
            print(f"'{option}' is not an option you may choose.\nPlease try again.")
            # continue to the next iteration of the while loop.