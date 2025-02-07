Code for the Bike shop with validations.

# Description:
# Author:
# Date(s):


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
        BikeType = input("Enter the bicycle type (T, M, B): ").upper()

        if BikeType != "T" and BikeType != "M" and BikeType != "B":
            print()
            print("    Data Enrty Error - Bicycle Type must be a T, M, or B.")
            print()
        else:
            break

    while True:
        try:
            NumBikes = input("Enter the number of bicycles rented (1 - 3): ")
            NumBikes = int(NumBikes)
        except:
            print()
            print("   Data Entry Error - Number of Bicycles is not a valid number.")
            print()
        else:
            if NumBikes < 1 or NumBikes > 3:
                print()
                print("   Data Entry Error - Number of Bicycles must be between 1 and 3.")
                print()
            else:
                break
            
    CCNum = input("Enter the credit card number (0000-0000-0000-0000): ")
    ExpDate = input("Enter the expiry date (MM/YY): ")

    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.
