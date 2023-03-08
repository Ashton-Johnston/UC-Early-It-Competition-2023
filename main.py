# -------------------------------------------------------------------------------------------------
# ----------------------------------- AJ Johnston -------------------------------------------------
# -------------------------------------------------------------------------------------------------
# ----------------------------- Last update on 3/8/2023 -------------------------------------------
# ----------------------------------- Version 2.3 -------------------------------------------------
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

# ask for the users name and write it to the output file
name = input("Enter the user's name: ")
output.write("Name: " + name)

while exitProgram == 0:  # make the loop for forever

    print("Your options are:")
    print("Rental")
    print("Guided [Tour]")
    print("Menu")
    print("[View] and confirm order")
    print("Exit")
    mainOption = input("Enter your option number here: ")

    # disregard case and use lowercase
    mainOption.lower()

    # rental
    if mainOption == "rental":                                                     # rental option
        # options
        print("Your options are: ")
        print("Jet Ski")
        print("Kayak")
        print("Paddle Board")

        # inputs
        selectedType = input("Enter your option here: ")
        numberOfHoursRental = input(str("Enter the number of hours wanted: "))
        dayOfRental = input("Enter day of rental: ")
        monthOfRental = input("Enter the month of rental: ")
        yearOfRental = input("Enter the year of rental: ")

        # disregard case sensitivity and use lowercase
        selectedType.lower()

        # select the value for the price
        if selectedType == "jet ski":
            option = price.jetSki
            output.write("\n" + "Jet Ski")
        elif selectedType == "kayak":
            option = price.kayak
            output.write("\n" + "Kayak")
        elif selectedType == "paddle board":
            option = price.paddleBoard
            output.write("\n" + "Paddle Board")
        else:
            print("Try Again!")

        # change things to displayable data
        dateOfRental = str("\n" + "Date: " + monthOfRental + "/" + dayOfRental + "/" + yearOfRental)
        totalPriceRental = str("\n" + "Price: " + str(numberOfHoursRental) * option)

        # print the stuff to the output file
        output.write(dateOfRental)
        output.write(totalPriceRental)

        # make the output easier to read
        print("\n")

    # Guided tour
    elif mainOption == "tour":                                                          # Guided tour option
        # options
        print("Your options are:")
        print("Scuba Diving")
        print("Parasailing")

        # inputs
        selectedType = input("Enter your option here: ")
        numberOfHoursTour = input("Enter the number of hours wanted: ")
        dayOfTour = input("Enter day of rental: ")
        monthOfTour = input("Enter the month of rental: ")
        yearOfTour = input("Enter the year of rental: ")

        #disregard case sensitivity and use lowercase
        selectedType.lower()

        # select value of the price
        if selectedType == "suba diving":
            option = price.scubaDiving
        elif selectedType == "parasailing":
            option = price.parasailing
        else:
            print("Try Again!")

        # change to displayable data
        dateOfTour = str("\n" + "Date: " + monthOfTour + "/" + dayOfTour + "/" + yearOfTour)
        totalPriceTour = str("\n" + "Price: " + str(numberOfHoursTour) * option)

        #write to the output file
        output.write(dateOfTour)
        output.write(totalPriceTour)

        # make the output easier to read
        print("\n")

    # menu
    elif mainOption == "menu":                                                          # menu option
        # options
        print("Your options are:")
        print("Canned Pop")
        print("Candy")
        print("Chips")
        print("Hot Dog")
        print("Cheeseburger")

        #get user input
        menuOption = input("Enter your option here: ")
        quantity = input("Enter quantity here: ")

        # disregard case and use lowercase
        menuOption.lower()

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
