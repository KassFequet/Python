# Main program starts here.# Description: QAP #3 - Honest Harry Car Sales
# Author: Kassaundra Fequet
# Date(s): February 7/25 -


# Define required libraries.
import datetime
import random
import math


# Define program constants.
MAX_SELL_PRICE = 50000.00



# Define program functions.



# Main program starts here.
CurDate = datetime.datetime.now()

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

    if FirstName.upper() == "END":
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
        elif PhoneNum.isdigit() == False: 
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
        elif (PlateNum[3:6]).isdigit() == False:
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
            print("   Data Entry Error - Car year must be entered ")
            print()
        elif len(CarYear) != 4:
            print()
            print("   Data Entry Error - Car year must be 4 digits only")
            print()
        elif CarYear.isdigit() == False:
            print()
            print("   Data Entry Error - Car year must be numbers")
            print()
        else:
            break
    
    while True:
        SellPrice = input("Enter the selling price: ")
    
        if SellPrice == "":
            print()
            print("   Data Entry Error - Sell price must be entered ")
            print()
        elif SellPrice.isdigit() == False:
            print()
            print("   Data Entry Error - Sell price must be numbers")
            print()
        else:
            SellPrice = float(SellPrice)
            if SellPrice > MAX_SELL_PRICE:
                print()
                print("   Data Entry Error - Sell price cannot exceed $50,000.00")
                print()
            else:
                break
            

    while True:
        TradeAmt = input("Enter the amount of the trade in: ")

        if TradeAmt == "":
            print()
            print("   Data Entry Error - Trade amount must be entered ")
            print()
        elif TradeAmt.isdigit() == False:
            print()
            print("   Data Entry Error - Trade amount must be numbers")
            print()
        else:
            TradeAmt = float(TradeAmt)
            if TradeAmt > SellPrice:
                print()
                print("   Data Entry Error - Trade amount cannot exceed the sell price")
                print()
            else:
                break

    while True: 
        SalesName = input("Enter the salespersons name: ")

        if SalesName == "":
            print()
            print("   Data Entry Error - Salespersons name must be entered ")
            print()
        else:
            break
        

    # Perform required calculations.
DateDsp = (CurDate.strftime("%B %d, %Y"))


    # Display results

print()
print(f"Honest Harry Car Sales                              Invoice Date:  ")



PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
print(PhoneNum)



    # Write the values to a data file for storage.



    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.
