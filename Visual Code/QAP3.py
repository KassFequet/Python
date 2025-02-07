# Description: QAP #3 - Honest Harry Car Sales
# Author: Kassaundra Fequet
# Date(s): February 7/25 -


# Define required libraries.



# Define program constants.



# Define program functions.



# Main program starts here.# Description: QAP #3 - Honest Harry Car Sales
# Author: Kassaundra Fequet
# Date(s): February 7/25 -


# Define required libraries.



# Define program constants.



# Define program functions.



# Main program starts here.
allowed_num = set("1234567890")

while True:

    # Gather user inputs.
    while True:
        FirstName = input("Enter the customers first name (or type 'END' to exit): ").title()

        if FirstName == "":
            print()
            print("   Data Entry Error - First name must be entered")
            print()
        else:
            break

    while True:
        LastName = input("Enter the customers last name: ").title()
    
        if LastName == "":
            print()
            print("   Data Entry Error - Last name must be entered")
            print()
        else:
            break
        
    while True:
        PhoneNum = input("Enter the customer phone number (0000000000): ")
        if PhoneNum == "":
            print()
            print("   Data Entry Error - Phone number must be entered.")
            print()
        elif len(PhoneNum) != 10:
            print()
            print("   Data Entry Error - Phone number must contain 10 digits only")
            print()
        elif set(PhoneNum).issubset(allowed_num) == False:
            print()
            print("   Data Entry Error - Phone number contains invalid characters")
            print()
        else:
            break


    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.