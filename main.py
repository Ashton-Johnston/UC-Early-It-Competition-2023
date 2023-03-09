# -------------------------------------------------------------------------------------------------
# ----------------------------------- AJ Johnston -------------------------------------------------
# -------------------------------------------------------------------------------------------------
# ----------------------------- Last update on 3/9/2023 -------------------------------------------
# ----------------------------------- Version 2.5 -------------------------------------------------
# -------------------------------------------------------------------------------------------------

# imports
import random
import time
import price

# variables
exitProgram = 0  # this stops the program
option = 0  # if option variable is needed this gets used

# ----------------------------------------- main code ---------------------------------------------


output = open("ShiningSeaOrder.txt", "w")  # open the output file

# make the welcome message
print("Welcome to Shining Sea Outfitters!")

# ask for the users name and write it to the output file
name = input("Please enter the user's name: ")
output.write("Name: " + name)

while exitProgram == 0:  # make the loop for forever

    print("!! Enter phrases that are in the [] brackets !!")
    print("Would you like to:")
    print("Book a [rental]")
    print("Book a guided [Tour]")
    print("view the [menu]")
    print("[view] and confirm order")
    print("or [exit]")
    rawMainOption = input("Enter your option here: ")

    # disregard case and use lowercase
    mainOption = rawMainOption.lower()

    # rental
    if mainOption == "rental":                                                     # rental option
        # options
        print("Would you like to: ")
        print("Rent a [jet ski]")
        print("Rent a [kayak]")
        print("Rent a [paddle board]")

        # inputs
        rawSelectedType = input("Enter your option here: ")
        numberOfHoursRental = int(input("Enter the number of hours wanted: "))
        date = input("Enter the date you want to rent on: ")

        # disregard case sensitivity and use lowercase
        selectedType = rawSelectedType.lower()

        # select the value for the price
        if selectedType == "jet ski":
            option = price.jetSki
            output.write("\n" + "Jet Ski ")
        elif selectedType == "kayak":
            option = price.kayak
            output.write("\n" + "Kayak")
        elif selectedType == "paddle board ":
            option = price.paddleBoard
            output.write("\n" + "Paddle Board ")
        else:
            print("Try Again!")

        # change things to displayable data
        totalPriceRental = "\n" + "Price: " + str(numberOfHoursRental * option)

        # print the stuff to the output file
        output.write(date)
        output.write(totalPriceRental)

        # make the output easier to read
        print("\n")

    # Guided tour
    elif mainOption == "tour":                                                          # Guided tour option
        # options
        print("Would you like to: ")
        print("Go on a [scuba diving] tour")
        print("or go on a [parasailing] tour")

        # inputs
        rawSelectedType = input("Enter your option here: ")
        numberOfHoursTour = input("Enter the number of hours wanted: ")
        date = input("Enter the date of the tour: ")

        #disregard case sensitivity and use lowercase
        selectedType = rawSelectedType.lower()

        # select value of the price
        if selectedType == "suba diving":
            option = price.scubaDiving
        elif selectedType == "parasailing":
            option = price.parasailing
        else:
            print("Try Again!")

        # change to displayable data
        totalPriceTour = str("\n" + "Price: " + str(numberOfHoursTour) * option)

        #write to the output file
        output.write(date)
        output.write(totalPriceTour)

        # make the output easier to read
        print("\n")

    # menu
    elif mainOption == "menu":                                                          # menu option
        # options
        print("Your menu options are:")
        print("[canned pop]")
        print("[candy]")
        print("[chips]")
        print("[hot dog]")
        print("[cheeseburger]")

        #get user input
        rawMenuOption = input("Enter your option here: ")
        quantity = input("Enter quantity here: ")

        # disregard case and use lowercase
        menuOption = rawMenuOption.lower()

        #get price of the item wanted
        if menuOption == "canned pop":
            option = price.cannedPop
            item = "Canned Pop"
        elif menuOption == "candy":
            option = price.candy
            item = "Candy"
        elif menuOption == "chips":
            option = price.chips
            item = "Chips"
        elif menuOption == "hot dog":
            option = price.hotDog
            item = "Hot Dog"
        elif menuOption == "cheeseburger":
            option = price.cheeseburger
            item = "Cheeseburger"
        else:
            print("Try Again!")

        # change to displayable data
        totalPriceMenu = str("\n" + "Price: " + quantity * option)

        # write to output
        output.write(totalPriceMenu)

        # make the output easier to read
        print("\n")

    # view the order and confirm
    elif mainOption == "view":                                               # view and confirm order
        output.close()
        print("Your current order is:")
        f = open('ShiningSeaOrder.txt', 'r')
        file_contents = f.read()
        print(file_contents)

        confirm = input("Is this order correct? [Enter yes or no] : ")

        if confirm == "yes":  # checks for yes or no and responds accordingly
            print("Order Placed.")
        elif confirm == "no":
            print("Please submit your order again.")
        else:
            print("That is not a valid option!")

        # make the output easier to read
        print("\n")

    # exit
    elif mainOption == "exit":                                                          # exit option
        print("Thanks for using the Shining Sea Outfitters program.")
        time.sleep(random.uniform(0, 1))
        quit()

    else:
        print("That is not a valid option!")

else:
    print("Thanks for using the Shining Sea Outfitters program.")
