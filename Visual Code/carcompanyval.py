# Description: Lesson 15/16 Car Company
# Author:KF
# Date(s): Feb 3/24


# Define required libraries.



# Define program constants.



# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    while True:
        CustName = input("Enter the customer name: ")

        if CustName == "":
            print()
            print("    Data Entry Error - Customer Name must be entered.")
            print()
        else:
            break

    while True:
        PhoneNum = input("Enter the customer phone number (0000000000): ")

        if PhoneNum == "":
            print()
            print("    Data Entry Error - Phone Number cannot be blank.")
            print()
        else:
            break
        
    while True:
        CarDetails = input("Enter the car year, make, and model: ")

        if CarDetails == "":
            print()
            print("    Data Entry Error - Car year, make, and model must be entered.")
            print()
        else:
            break

    while True:
        CarPrice = input("Enter the price of the car: ")
        
        try:
            CarPrice = float(CarPrice)
            if CarPrice < 1000 or CarPrice > 10000:
                print()
                print("    Data Entry Error - Car price must be between $1000 and $10000.")
                print()
            else:
                break
        except ValueError:
            print()
            print("    Data Entry Error - Please enter a valid number for the car price.")
            print()

# Perform required calculations.



# Display results



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.