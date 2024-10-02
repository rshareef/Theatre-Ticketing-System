# IN0005 FINAL PROJECT: MILESTONE 2

# COMMON MODULE (i.e. functions that are used commonly by both Normal Users and Admin Users).
# This module is imported to both 'admin_module' and 'normal_user_module'.

### REFERENCES USED:
    # Checking if a file exists: https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/
    # Understanding how 'with open' works: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
    # Using the json module: https://www.freecodecamp.org/news/how-to-use-the-json-module-in-python/#:~:text=dump()%20function-,The%20json.,the%20data%20will%20be%20written.
    # Understanding ValueError: https://docs.python.org/3/library/exceptions.html

### IMPORTS
# import json module to be used by the functions 'loadData' and 'dumpData' (defined below).
import json
# import the module 'os.path' (for checking if the text files "bookings.txt" and "usernames.txt" exist) in the 'initialiseFiles' function (defined below).
import os.path
# import the module 'sys' for use by the 'quitProgram' function (defined below).
import sys


### FUNCTIONS
# FUNCTION PURPOSE: Load all the data from the specified file (passed into function as the argument 'filename'), into a variable for manipulation.
def loadData(filename):
    # Parameters:
        # filename (string): This parameter is used for identifying the specific file to load data from (either "bookings.txt" or "usernames.txt").
    
    # open the file 'filename' in read mode and assign to the variable 'file'.
    with open(filename, "r") as file:
        # load the list data structure from the file, into a variable.
        newdata = json.load(file)
    # file will close automatically due to the 'with' statement above.
    # return variable that contains the list.
    return newdata


# FUNCTION PURPOSE: Write the list stored in the variable 'data' (passed into function as an argument), into the specified file (passed into function as the argument 'filename').
def dumpData(filename, data):
    # Parameters:
        # filename (string): This parameter is used for identifying the specific file to dump data to (either "bookings.txt" or "usernames.txt").
        # data (list): This parameter is used to hold the data that is to be dumped (stored directly) into the file.
    
    # open thefile 'filename' in write mode and assign to the variable 'file'.
    with open (filename, "w") as file:
        # dump variable 'data' that holds the list, into the file.
        json.dump(data, file)
    # file will close automatically due to the 'with' statement above.


# FUNCTION PURPOSE: To terminate the program.
def quitProgram():
    # output a message for the user.
    print("Program Terminated.")
    # 'sys.exit()' accesses the function 'exit()', from the module 'sys', to terminate the program.
    sys.exit()


# FUNCTION PURPOSE: Initialise the theatre seating arrangement into a 2D list.
def initialiseTheatre():
    # initialise an empty list, for appending the list generated (in each iteration of the nested for loop) below to.
    # this will result in the variable 'theatre_list' containing a 2D list, with sub-lists representing individual seats.
    theatre_list = []
    
    # Format of a seat (i.e. a sub-list of 'theatre-list'): [username, row_no , seat_no, seat_price]: e.g. ["Ruqayyah",5,3,60].
    # Each seat (sub-list) will contain the following data values:
    # seat[0] = username: at initialisation, usernames in every sub-list will be set to "". 
    # seat[1] = row_no: row numbers range from: 1 to 7.
    # seat[2] = seat_no: seat numbers range from: 1 to (6 + (2 * row_no)). The formula '(6 + (2 * row_no))' calculates the correct number of seats in each row.
    # seat[3] = seat_price: seat prices based on 'row_no' will be stored in a dictionary for convenient price value retrival (a dictionary can be used because: row numbers are unique, thus keys can be unique).
    
    # creating dictionary to store row number and corresponding seat price (in GBP).
    prices = {
        1 : 100,
        2 : 80,
        3 : 70,
        4 : 70,
        5 : 60,
        6 : 40,
        7 : 20
        }
    
    # generate seats (sub-lists).
    # for every row, from row 1 to row 7:
    for row in range (1,8):
        # for each seat, from seat 1 to seat (6 + (2 * row)):
        for seat in range (1,(6 + (2 * row))+1):
            # assign the data values for this seat (sub-list).
            seat_list = ["", row, seat, prices[row]]
            # append the sub-list 'seat_list' to main list 'theatre_list'.
            theatre_list.append(seat_list)
    
    # 'theatre_list' creation is now complete. save the 2D list in the file "bookings.txt".
    dumpData("bookings.txt", theatre_list)
    

# THIS FUNCTION ('initialiseFiles') HAS BEEN ADDED SINCE MILESTONE 1.
# FUNCTION PURPOSE: Initialise the text files "usernames.txt" and "bookings.txt", and their starting contents (for the initial running of the program).
def initialiseFiles():
    # checking if "usernames.txt" exists:
    # we want to check if "usernames.txt" exists in the same folder/level as our 'main_program.py' and modules, so pass the path as an argument into the function 'os.path.isfile'.
    # assign the Boolean value returned from the function 'os.path.isfile("./usernames.txt")' to the variable 'check_user_file'.
    check_user_file = os.path.isfile("./usernames.txt")

    # checking if "bookings.txt" exists:
    # we want to check if "bookings.txt" exists in the same folder/level as our 'main_program.py' and modules, so pass the path as an argument into the function 'os.path.isfile'.
    # assign the Boolean value returned from the function 'os.path.isfile("./bookings.txt")' to the variable 'check_bookings_file'.
    check_bookings_file = os.path.isfile("./bookings.txt")

    # if "usernames.txt" does not exist AND/OR "bookings.txt" does not exist, initialise both text files.
    if check_user_file == False or check_bookings_file == False:
        print("Initialising Text Files...")
        
        # use the 'dumpData' function to create the file "usernames.txt", and save an empty list to the file.
        dumpData("usernames.txt", [])
        
        # initialise "bookings.txt" by calling the 'initialiseTheatre()' function.
        initialiseTheatre()
        
        # NOTE: 'dumpData', used above to initialise the "usernames.txt" file and within initialiseTheatre() to initialise "bookings.txt", opens files in write mode which prevents an error for example if 1 file exists and the other does not, but we want them to both be initialised.
        print("Text Files Initialised.")
    # if both files exist in the same folder/level as our 'main_program.py' and modules, we just output a message to confirm this to the user.
    else:
        print("Text Files Already Initialised.")


# FUNCTION PURPOSE: Print the theatre layout in the desired format.
def printTheatre(itemSearched, printResult):
    # Parameters:
        # itemSearched (string): This parameter will either hold the value of "" or {username}.
        # printResult (string): This parameter will hold what we would like printed in the theatre layout when the {itemSearched} is matched to that seat.
    
    # There are two versions of printing:
        # 1. Showing ALL the bookings, with an 'x'. [printTheatre("", "x")]
        # 2. Showing an individual USER'S bookings, with a 'B'. [printTheatre({username}, "B")]
    
    # load the data from "bookings.txt" and assign the result to the variable 'data'.
    data = loadData("bookings.txt")

    # printing the theatre:
    # create a margin at the top for visual clarity.
    print("\n")
    # initialise a string for appropriate indenting of each row. initialised with two spaces so theatre layout is displayed overall with a slight margin from the left edge of the console.
    spacing_string = "  "
    # for every row in the theatre (starting from row 7 and decrementing by 1 row each iteration, till row 1).
    for row in range (7,0,-1):
        # calculate the total number of seats present in the current row iteration.
        total_seats = (6 + (2 * row))
        # create the sub-list 'row_list' from the original list 'data', to iterate through in the for loop below (sub-list will only contain list elements relevant to the row number of the current iteration).
        # e.g. the first sub-list created will need to be for row 7. There are 20 seats (calculated by 'total_seats' above) in row 7 so, the sub-list will contain the last 20 elements of the original list 'data'.
        row_list = data[-total_seats:]
        # now that we have created the sub-list to iterate through, we will remove those exact elements (now in the sub-list that was just created) from the original 'data' list. ('data' has just been read from the text file into a variable, so we do not need to worry about conflicting changes in the actual file).
        data = data[:-total_seats]
        # at the start of every row, output the 'spacing_string' to appropriately indent each row for the correct printed layout. ('end' parameter changes the end character from a newline character (default) to an empty string (i.e. prints nothing extra after the main content)).
        print(spacing_string, end = "")


        # loop through all of the elements in the 2D list 'row_list'(i.e. seats for current row only).
        for seat in row_list:
            # determine the condition (which depends on the itemSearched) for printing the {printResult}:
            if itemSearched == "":
                printCondition = (seat[0] != "")
            else:
                printCondition = (seat[0] == itemSearched)
                
            # printing the appropriate character to represent this seat along with a single space to conform to desired layout.
            # if the printCondition is True, then print the {printResult} for that seat.
            if printCondition == True:
                print(printResult, end = " ")
            # otherwise, print a blank seat "_", for that position.
            else:
                print("_", end = " ")
            
            # (i.e. if the current_iterated_username != "": 
            #           print "x"
            #       else: 
            #           print "_").
            # OR
            # (i.e. if the current_iterated_username == username passed into the function:
            #           print "B"
            #       else:
            #           print "_").
                   
            # Continue to the next iteration of the innermost for loop.

        # extend the current spacing string by two spaces (to consider for the extra two seats removed as we descend to the next row).
        spacing_string = spacing_string + "  "
        # output a newline character to begin a new row.
        print("\n")
        # continue to next iteration of outermost for loop.


# FUNCTION PURPOSE: To ask the user to enter a row and seat number, validate the row and seat number entry given by a user, and then check if the seat is booked or not.
def validateSeatEntry(username = "", user_booked_only = False):
    # Parameters:
        # username = "" (string, OPTIONAL PARAMETER): This parameter is optionally provided when the user is a normal user, so that we can use their username to search for the tickets they specifically have booked.
        
        # PARAMETER ADDED SINCE MILESTONE 1:
        # user_booked_only = False (Boolean, OPTIONAL PARAMETER): This parameter is optionally provided when the user is a normal user, AND the 'cancelTicket' function is called. It informs the desicion made in this function ('validateSeatEntry') regarding the condition to be checked against the selected seat.
        # It holds the default value 'False'. When the parameter needs to be used, I will provide the argument value of 'True' in the function call to override this default.
    
    # ROW NUMBER VALIDATION
    # loop until a valid entry has been provided.
    while True:
        # handle any potential exceptions or errors generated from user input with a try-except-else clause.
        try:
            # ask the user what ROW number they would like to choose.
            row = int(input("\nPlease enter the number corresponding to the row (from 1-7), you would like to choose:\n>>>"))
        # if a ValueError is raised, catch the error with the 'except' clause.
        # e.g. will be raised when a user provides an incorrect value to the int() function : i.e. letter(s) / a floating point number / a special character.
        except ValueError:
            # output a message to the user and continue to the next iteration of the while loop.
            print("\nYour input is not an integer. Please try again.")
        # otherwise, if a ValueError has not been raised in this while loop iteration, check that the integer entered is between 1 and 7 (so that it matches a row number).
        else:
            # if the user input is NOT between 1 and 7, output a message to the user and continue to the next iteration of the while loop.
            if row not in range(1,8):
                print("\nYour entry is not in the range 1-7. Please try again.")
            # otherwise, (i.e. the user input is overall valid), exit the while loop.
            else:
                break
    # SEAT NUMBER VALIDATION
    # (NOTE: as this code is very similar to the row number validation, I could create a function for the above code to reuse, however I have chosen not to for simplicity, clarity and because it would not make my code that much more efficient as I would still have to pass variables into the function as they are slightly different cases).
    # now that the user has entered a valid row number, we can calculate the total number of seats that exist on the user's selected row and assign the result to the variable 'total_seats'.
    total_seats = (6 + (2 * row))
    # loop until a valid entry has been provided.
    while True:
        # handle any potential exceptions or errors generated from user input with a try-except-else clause.
        try:
            # ask the user what SEAT number they would like to choose.
            seat = int(input(f"\nPlease enter the number corresponding to the seat (from 1-{total_seats}), you would like to choose:\n>>>"))
        # if a ValueError is raised, catch the error with the 'except' clause.
        # e.g. will be raised when a user provides an incorrect value to the int() function : i.e. letter(s) / a floating point number / a special character.
        except ValueError:
            # output a message to the user and continue to the next iteration of the while loop.
            print("\nYour input is not an integer. Please try again.")
        # otherwise, if a ValueError has not been raised in this while loop iteration, check that the integer entered is between 1 and total_seats (so that it matches a seat number).
        else:
            # if the user input is NOT between 1 and total_seats, output a message to the user and continue to the next iteration of the while loop.
            if seat not in range(1, total_seats+1):
                print(f"\nYour entry is not in the range 1-{total_seats}. Please try again.")
            # otherwise, (i.e. the user input is overall valid), exit the while loop.
            else:
                break
    
    # now we know the user entry is valid, check if the seat has already been booked.
    
    # load the data from "bookings.txt" and search for the row and seat number.
    data = loadData("bookings.txt")
    
    # to search for the seat, we need to find the index of the list element in 'data' representing the seat with the chosen row and seat number.
    # to do this, we can use the formula: (sum of all the seats in the rows before chosen row [starting from row 1 and ending at row 7] + chosen seat number) - 1 (as indexing of the list 'data' starts from 0), to find the correct list index of the chosen seat.
    # total_prev_rows = sum of all the seats in the rows before chosen row [starting from row 1 and ending at row 7]:
    total_prev_rows = 0
    # for each row until the row before the row of the chosen seat:
    for i in range (1,row):
        total_prev_rows = total_prev_rows + (6 + (2 * i))
    
    # thus, using formula stated above, the index of the seat with this row and seat number:
    index = (total_prev_rows + seat) - 1
    
    # now that we have found the index of the desired list element, we can check if that seat has been booked.
    # if a value for 'user_booked_only' has been provided through an optional argument during the function call (i.e. user_booked_only = True):
    if user_booked_only:
        # set the condition to be checked, to: the username at index [0] in the selected list element of 'data' matches the username passed into the function.
        condition = (data[index][0] == username)
    # if no username has been provided (i.e. user_booked_only holds a default value of False).
    else:
        # set the condition to be checked, to: the username at index [0] in the selected list element of 'data' is not a blank string.
        condition = (data[index][0] != "")
    
    # if the seat has been booked (i.e. condition = True), set the 'booked' variable to 'True'.
    if condition:
        # 'booked = True' indicates the seat has been booked.
        booked = True
    # otherwise, (i.e. condition = False) set the 'booked' variable to 'False'.
    else:
        # 'booked = False' indicates the seat has not been booked.
        booked = False
    # return: booked, row, seat, price, index ('index' was added going from Milestone 1 to Milestone 2, so that the calculated index can easily be re-used).
    return booked, row, seat, data[index][3], index


# FUNCTION PURPOSE: To allow an admin or a normal user to cancel a ticket.
def cancelTicket(username = ""):
    # Parameters:
        # username = "" (string, OPTIONAL PARAMETER): This parameter is optionally provided when the user is a normal user, so that we can use their username to search for the tickets they specifically have booked (passed as an argument to validateSeatEntry()).
        
        # REMOVED PARAMETER BELOW: (userType). I recognised this was not nessecary as we may differentiate between a normal and admin user depending on if a username is provided or not when the function is invoked from their respective main menu.
        # (userType(string): This parameter is used to determine if the user is an admin or a normal user. The value will be set as an argument in their respective menu option function.)
        
    
    # (NOTE: I recognise that I have performed this style of check in the 'bookTicket' [normal_user_module] and 'reset' [admin_module] functions. I could create a function to re-use, however since the cases are only half-similar, more customised and not that lengthy, for simplicity and clarity I have not created a function for this process).
    # check that there are tickets available to cancel (to prevent the user being stuck in a loop of asking them to provide a valid seat to cancel).
    # flag 'continueCancel' to determine whether to proceed to cancelling tickets or exit the function.
    continueCancel = True
    # load the bookings data from "bookings.txt" into the variable 'data'.
    data = loadData ("bookings.txt")
    # initialise variable to keep count of the running total of empty seats in the theatre.
    emptySeats = 0
    
    # check each seat in the theatre.
    for seat in data:
        # if the seat has been booked by the username passed into the parameter, increment the empty seat counter by 1.
        # if the 'cancelTicket' function was called by an ADMIN user, no username argument would be provided, thus username has a default value of "".
        # if the 'cancelTicket' function was called by a NORMAL user, a username argument will be provided.
        if (seat[0] == username):
            emptySeats = emptySeats + 1
            
    # determine the total count of empty seats we are looking for depending on the type of user.
    if username == "":
        # for an admin: the total count indicating an empty theatre is 98 because in the above 'if' statement we are counting the number of blank seats (which would be 98 if the theatre was empty).
        result = 98
    else:
        # for a normal user: the total count indicating an empty theatre is 0 because in the above 'if' statement we are counting the number of seats booked under that username (which would be 0 if the user has not booked any seats, so cannot cancel any).
        result = 0
    # if there are no tickets the user can cancel.
    if emptySeats == result:
        # output a message to the user.
        print("\nThere are no booked tickets that you can cancel.")
        # and do not start the ticket cancellation process.
        continueCancel = False
    
    # if there are any tickets that can be cancelled in the theatre by this user, we may start the potential cancellation process.
    if continueCancel == True:
        # determine if the user is an admin or normal user based on if a username has been provided as an argument upon function invocation.
        # then assign the appropriate value for that type of user to printResult (i.e. what we would like printed on the theatre layout for tickets that user is able to cancel).
        # if the user is an admin user.
        if username == "":
            printResult = "x"
        # if the user is a normal user.
        else:
            printResult = "B"

        # call the function: 'printTheatre(itemSearched, printResult)', to show tickets that have been booked.
        printTheatre(username, printResult)
        
        # establish a while loop.
        while True:
            # call the function 'validateSeatEntry()' for an admin user.
            if username == "":
                booked, row, seat, price, index = validateSeatEntry()
            # call the function 'validateSeatEntry(username, True)' if the user is normal.
            else:
                booked, row, seat, price, index = validateSeatEntry(username, True)
            # in both cases assign the returned values to variables: booked, row, seat, price, index (this was added going from Milestone 1 to Milestone 2, so that the calculated index can easily be re-used).    
            
            # if the seat has not been booked, (booked == False), the ticket cannot be cancelled.
            # so, output a message for the user and continue to the next iteration of the while loop.
            if booked == False:
                print("\nYou cannot cancel this seat because it has not been booked.\nPlease try again.\n")

            # if the seat has been booked, (booked == True), then print out information for that seat:
               # Row: {row}
               # Seat: {seat}
               # Price: £{price}
            # and exit the while loop.
            else:
                print(f"\nRow: {row}\nSeat: {seat}\nPrice: £{price}")
                break
        
        # asking for user confirmation before they cancel the ticket.        
        while True:
            confirm = input('''
Are you sure you want to cancel this ticket? (Y/N)
Enter the letter that corresponds with your choice, e.g. "N":
    Y - Yes
    N - No
>>>''')
            
            # NOTE: I have applied both '.upper()' and '.strip()' functions to the user input 'confirm' to accept the user's input even if they have used lowercase 'y/n' instead, or have any leading/ending whitespaces in their input, and have stored this in the variable 'modifiedInput'.
            modifiedInput = (confirm.upper()).strip()
            # if the user confirms:
            if modifiedInput == "Y":
                # change the value of the username index in that seat, to "".
                data[index][0] = ""
                # save the bookings data back into the "bookings.txt" file.
                dumpData ("bookings.txt", data)
                # output a message to the user confirming the ticket was cancelled.
                print("Ticket cancelled.")
                # exit the while loop.
                break
            # if the user chooses to not confirm:
            elif modifiedInput == "N":
                # output a message to the user confirming the ticket was NOT cancelled.
                print("Ticket not cancelled.")
                # exit the while loop.
                break
            # if the user has provided any input other than Y or N (i.e. an invalid input).
            else:
                # output a message to the user.
                print(f"'{confirm}' is not an option you may choose.\nPlease try again.")
                # continue to the next iteration of the while loop.
    # the user will be returned to the main menu automatically, once the function has completed execution.