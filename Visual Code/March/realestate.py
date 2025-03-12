# Description: Real Estate
# Author: Mo and Class
# Date(s): Mar 11/25


# Define required libraries.
import datetime


# Define program constants.
CUR_DATE = datetime.datetime.now()


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    ListNum = input("Enter the listing number(999999999): ")
    StAdd = input("Enter the street address: ")
    NumBed = input("Enter the number of bedroom: ")
    NumBath = input("Enter the number of bathrooms: ")
    TotSqFeet = input("Enter the total square footage: ")
    
    DateLst = []
    PriceLst = []
    while True:
        while True:
            try:
                ListDate = input("Enter the listing date (YYYY-MM-DD): ")
                ListDate = datetime.datetime.strptime(ListDate, "%Y-%m-%d")
            except:
                print()
                print("   Data entry Error - List Date not a valid date")
                print()
            else:
                if ListDate > CUR_DATE:
                    print()
                    print("   Data Entry Error - List date cannot be in future")
                    print()
                else:
                    break
        
        while True:
            try:
                ListPrice = input("Enter the list price: ")
                ListPrice = float(ListPrice)
            except:
                print()
                print("   Data Entry Error - List Price is not a vlaid number")
                print()
            else:
                break
        
        DateLst.append(ListDate)
        PriceLst.append(ListPrice)
        
        Continue = input("Enter another listing date and price (Y/N): ").upper()
        if Continue == "N":
            break

    StatusLst = ["Open", "Offer Pending", "Sold"]
    while True:
        Status = input("Enter the status (Open, Offer Pending, Sold): ").title()
        
        if Status not in StatusLst:
            print()
            print("   Data Entry Error - Invalid Entry for the Status")
            print()
        else:
            break
        
    

    #Perform required calculations.



    # Display results
    print()
    print(DateLst)
    print(PriceLst)
    print(Status)
    print()


    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.