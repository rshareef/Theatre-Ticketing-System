# IN0005 FINAL PROJECT: MILESTONE 2
# NOTE: the name of this module was changed between Milestone 1 and Milestone 2 from: 'normal_module.py' to 'normal_user_module.py' for improved naming clarity.

# NORMAL USER MODULE (i.e. functions that are used by only Normal Users).

### IMPORTS
# functions from 'common_module' are referenced within this module, so I have imported it with a shorthand to make it clear which functions have been imported into this module.
import common_module as cm

### FUNCTIONS
# FUNCTION PURPOSE: To allow the user to book a ticket.
def bookTicket(username):
    # Parameters:
    # username (string): This parameter is used for when the user confirms to book a ticket. The 'username' will be saved in "bookings.txt" with the selected seat and row number.
    
    # check if the theatre is already full (i.e. there are no more seats that can be booked).
    # flag 'continueBook' to determine whether to proceed to ticket booking process or exit the function.
    continueBook = True
    # load the theatre bookings 2D list from "bookings.txt" by calling 'loadData("bookings.txt")' [imported from 'common_module'] and assign the return value to the variable 'data'.
    data = cm.loadData ("bookings.txt")
    # initialise variable to keep count of the running total of booked seats in the theatre.
    bookedSeats = 0
    # check each seat in the theatre.
    for seat in data:
        # if the seat has been booked by anyone (i.e. the username index of the seat sublist is not empty), increment the booked seat counter by 1.
        if seat[0] != "":
            bookedSeats = bookedSeats + 1
    # if the total number of booked seats in the theatre is 98, this indicates the theatre is full.
    if bookedSeats == 98:
        # so, output a message to the user that they cannot book any tickets as the theatre is full.
        print("\nThere are no empty seats to book in the theatre. Theatre full.")
        # and do not start the ticket booking process.
        continueBook = False
    
    # if there are any empty seats in the theatre, we may start the potential ticket booking process.
    if continueBook == True:
        # display current booking status for the theatre (the already booked seats are marked with the symbol x). [printTheatre has been imported from 'common_module'].
        cm.printTheatre("","x")
        # establish a while loop.
        while True:
            # call the function 'validateSeatEntry' [imported from 'common_module'], and assign the returned values to variables: booked, row, seat, price, index.
            booked, row, seat, price, index = cm.validateSeatEntry()

            # if the seat has been booked, (booked == True):
            if booked == True:
                # output a message to the user stating that the seat has been booked.
                print("\nThis seat is booked.\nPlease try again.")
                # continue to the next iteration of the while loop.
                
            # if the seat has NOT been booked (booked == False):
            else:
                # show the user the price of the seat
                print(f"Price of seat: £{price}")
                # exit the while loop.
                break
            
        # ask the user to confirm their seat booking choice.
        while True:
           # ask the user to confirm that they want to book this ticket.
            confirm = input(f'''
Are you sure you want to book this ticket?
Row: {row}
Seat: {seat}
Price: £{price}

Enter the letter that corresponds with your choice, e.g. "N":
    Y - Yes
    N - No
>>>''')
    
            # NOTE: I have applied both '.upper()' and '.strip()' functions to the user input 'confirm' to accept the user's input even if they have used lowercase 'y/n' instead, or have any leading/ending whitespaces in their input, and have stored this in the variable 'modifiedInput'.
            modifiedInput = (confirm.upper()).strip()
            
            # if the user confirms the ticket booking:
            if modifiedInput == "Y":
                # change value of the username index of the selected seat (blank string), to the 'username' argument passed into the function.
                data[index][0] = username
                # save the bookings data back into the "bookings.txt" file using the function 'dumpData' [imported from 'common_module'].
                cm.dumpData ("bookings.txt", data)
                # output a message to the user confirming that the ticket was booked.
                print("Ticket successfully booked.")
                # exit the while loop.
                break
            # if the user chooses to NOT confirm:
            elif modifiedInput == "N":
                # output a message to the user confirming that the ticket was not booked.
                print("Ticket booking cancelled.")
                # exit the while loop.
                break
            # if the user enters anything else (i.e. an invalid input):
            else:
                # output a message to the user stating their input is not an option.
                print(f"'{confirm}' is not an option you may choose.\nPlease try again.")
                # continue to the next iteration of the while loop.
                
    # the user will be returned to the main menu automatically, once the function has completed execution.


# FUNCTION PURPOSE: To output details of the tickets bought by the user.
def showTicket(username):
    # Parameters:
    # username (string): This parameter is used for the username we wish to find a match for in the seat booking data, to determine which seats this user has booked.
    
    # load the theatre bookings 2D list from "bookings.txt" by calling the function 'loadData' [imported from 'common_module'] and assign the return value to the variable 'data'.
    data = cm.loadData("bookings.txt")
    # establish a counter variable, for printing out the ticket number.
    counter = 1
    # loop through each list element of the 2D list 'data' to check for seats booked under the name 'username'.
    for seat in data:
        # if the current seat iteration is booked under 'username':
        if seat[0] == username:
            # output the information for that seat:
            print(f"""  
Ticket {counter}
Row: {seat[1]}
Seat: {seat[2]}
Price: £{seat[3]}
--------------""")
            # increment the counter by 1 (for the next potential ticket found to be booked under 'username').
            counter = counter + 1
    
        # if the current seat iteration is NOT booked under 'username'
        # continue to the next iteration of the for loop.
        
    # after iterating through all of the username indexes in the bookings data, if there are no tickets to show:
    if counter-1 == 0:
        # output a message for the user.
        print("You have not booked any tickets yet.")
    # otherwise, if there are tickets found and displayed for the user, allow the user to control when they would like to return to the main menu.
    else:    
        # ask the user to press enter to return to the main menu. (since Milestone 1: 'press any key' has been changed to 'press enter' for simplicity as the user must press enter in the console anyway for input to be accepted).
        input("\nPress enter to return to the main menu.")
    # the user will be returned to the main menu automatically, once the function has completed execution.


# FUNCTION PURPOSE: To display the option menu for a normal user and run the function corresponding to their input choice.
def normalOptionMenu(username):
    # Parameters:
    # username (string): This parameter is used to pass the value of the username through to the function option the user will choose.
    
    # establish a while loop. loop until the user chooses to quit (option 4).
    while True:
        # print out an option menu and ask the user to enter a number corresponding to their functionality choice.
        option = input('''
Main Menu
Please enter a number from 1-4 that matches your option choice:
1. Book Ticket
2. Cancel ticket
3. Show Ticket
4. Quit
>>>''')
        # NOTE: I have applied the '.strip()' function to the user input 'option' to accept the user's input even if they have any leading/ending whitespaces in their entry.
        option = option.strip()
        
        # if the user has chosen a valid option (number from 1-4), invoke the correct function for the option selected.
        if option == "1":
            bookTicket(username)
        elif option == "2":
            cm.cancelTicket(username)
        elif option == "3":
            showTicket(username)
        elif option == "4":
            cm.quitProgram()
        
        # if the user enters anything else (i.e. an invalid input):
        else:
            # output a message to the user stating their input is not an option.
            print(f"'{option}' is not an option you may choose.\nPlease try again.")
            # continue to the next iteration of the while loop.


# FUNCTION PURPOSE: To validate the entry of a username for both new and existing users.
def username(condition):
    # Parameters:
    # condition (Boolean): This parameter is used to describe the outcome we desire when the user has entered the appropriate username for their user status:
       # - new users are registering, so when the username they enter gets checked if it exists, a value of False indicates it does not exist, which is what we want.
       # - existing users are logging-in, so when the username they enter gets checked if it exists, a value of True indicates it exists, which is what we want.
    
    # establish a flag variable for the boolean state of the username existing or not.
    # assume that the username does not exist (exists = False).
    exists = False
    
    # load the usernames list from "usernames.txt" by calling the function 'loadData' [imported from 'common_module'] and assigning the return value to the variable 'username_list'.
    username_list = cm.loadData("usernames.txt")
    
    # if the user is an existing user, but no usernames have been registered (usernames list is empty) - this is not possible (the user may have entered their choice in wrong).
    if condition == True and username_list == []:
        # so, output a message for the user.
        print("No users have been registered. Please register before trying to log-in as an existing user.")
        # re-assign the value of their condition parameter passed in as 'True' to 'False' (they are now treated as a new user), and proceed to register the user.
        condition = False
    
    # establish a flag variable to control the while loop.
    loop = False
    # begin a while loop.
    while loop == False:
        # ask the user to enter a username OR allow the user to go back to choosing if they are a new or existing user, incase they made an input error.
        name = input("\n(Type 'B' to go back to choosing if you are a new/existing user)\nOR\nPlease enter your preferred username:\n>>>")
        # remove any leading/ending whitespace from the username to avoid potential errors later on.
        name = name.strip()
        
        # if the user has chosen to go back, return them to the normal user type choice stage:
        if name.upper() == "B":
            break

        # otherwise proceed with username stage:
        else:
            # check if the user entered username exits in the list variable 'username_list'.
            # if it does, then set flag variable 'exists' to True.
            if name in username_list:
                exists = True
            # if it does not, ensure variable 'exists' is False (must set it explicitly incase in the last iteration the name was found in 'username_list').
            else:
                exists = False
            
            # compare the 'exists' flag to the 'condition' parameter passed into the function, to check if they match.
            # if they do match, then we have acheived the desired user input: so call the menu function 'normalOptionMenu', with the argument 'name' to pass on the user's username to other functions for later use, where nessecary.
            if exists == condition:
                # set flag variable 'loop' to 'True' to prevent another iteration.
                loop = True
                # only if the user is a new user (i.e condition = False), additionally:
                if condition == False:
                    # add their username to the list of existing usernames.
                    username_list.append(name)
                    # save the updated usernames list in the file "usernames.txt" with the function 'dumpData' [imported from 'common_module'].
                    cm.dumpData("usernames.txt", username_list)
                    # output a message to the user.
                    print(f"\n{name}, you have been sucessfully registered!")
                # otherwise, if the user is an existing user:
                else:
                    # output a message to the user.
                    print(f"\n{name}, you have been sucessfully logged-in!")
                # go to the main menu for a normal user.
                normalOptionMenu(name)
                
            # if they do not match, output an appropriate message for the user, depending on whether they are a new/existing user.
            else:
                # if the user is a new user:
                if condition == False:
                    print("\nThis username already exists.\nPlease try again.")
                # if the user is an existing user:
                else:
                    print("\nThis username is not registered.\nPlease try again.")
                    # move to the next iteration of the while loop (i.e. repeat the process of this function until we get the desired input).


# FUNCTION PURPOSE: For a normal user to either: register or log-in.
def normalUserProgramEntry():    
    # check if the user is a new user.
    # loop until a valid input is provided.
    while True:
        # ask the user to provide input.
        newUser = input('''
Are you a new user? (Y/N)
Enter the letter that corresponds with your choice, e.g. "N":
    Y - New user
    N - Existing user
(or B - Go back to choosing user type)
>>>''')
        # NOTE: I have applied both '.upper()' and '.strip()' functions to the user input 'newUser' to accept the user's input even if they have used lowercase 'y/n' instead, or have any leading/ending whitespaces in their input, and have stored this in the variable 'modifiedInput'.
        modifiedInput = (newUser.upper()).strip()
        
        # all of the functions invoked as a result of a valid input will eventually quit the program for the user when they decide to quit at whatever stage, using the function 'quitProgram'.
        # if they are a NEW user, register: call the function 'username' with the boolean argument 'False': 'username(False)'.
        if modifiedInput == "Y":
            # i.e. we want the username entered by a NEW user to not exist already (argument for 'username' = False).
            username(False)
        # if they are not a new user, log-in: call the function 'username' with the boolean argument 'True': 'username(True)'
        elif modifiedInput == "N":
            # i.e. we want the username entered by an EXISTING user to exist already (argument for 'username' = True).
            username(True)
        # give the user the opportunity to go back, e.g. if they entered their user type incorrectly.
        elif modifiedInput == "B":
            # exit this while loop. then the user will be returned to choosing their user type (admin/normal).
            break
        # otherwise if the user input is invalid, output a statement for the user.
        else:
            print(f"'{newUser}' is not an option you may choose.\nPlease try again.")
            # continue to the next iteration of the while loop.