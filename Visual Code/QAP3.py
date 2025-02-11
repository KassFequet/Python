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
allowed_upper_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_upper_lower_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


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
        
    while True:
        PlateNum = input("Enter the plate number (XXX000): ").upper()

        if PlateNum == "":
            print()
            print("   Data Entry Error - Plate number must be entered ")
            print()
        elif len(PlateNum) != 6:
            print()
            print("   Data Entry Error - Plate number must be 6 characters only")
            print()
        elif set(PlateNum[0:3]).issubset(allowed_upper_lower_char) == False:
            print()
            print("   Data Entry Error - Plate number must start with 3 letters")
            print()
        elif set(PlateNum[3:6]).issubset(allowed_num) == False:
            print()
            print("   Data Entry Error - Plate number must end with 3 numbers")
            print()
        else:
            break
        
    while True:
        CarMake = input("Enter the car make: ")
        
        if CarMake == "":
            print()
            print("   Data Entry Error - Car make must be entered ")
            print()
        elif set(CarMake).issubset(allowed_upper_lower_char) == False:
            print()
            print("   Data Entry Error - Car make must be letters")
            print()
        else:
            break
        
    while True:
        CarModel = input("Enter the car model: ")
        
        if CarMake == "":
            print()
            print("   Data Entry Error - Car model must be entered ")
            print()
        else:
            break
        
    
    while True:
        CarYear = input("Enter the car year: ")
        
        if CarYear == "":
            print()
            print("   Data Entry Error - CarYear must be entered ")
            print()
        elif len(PlateNum) != 4:
            print()
            print("   Data Entry Error - Car year must be 4 characters only")
            print()
        elif set(CarYear).issubset(allowed_num) == False:
            print()
            print("   Data Entry Error - Car year must be numbers")
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