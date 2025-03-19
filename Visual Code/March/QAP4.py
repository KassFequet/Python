# Description: QAP 4 - Car Insurance Policy
# Author: Kassaundra Fequet
# Date(s): March 14/25 - 


# Define required libraries.
import FormatValues as FV
import datetime as DT


# Define program constants.
POL_NO = 1944
BASIC_PRE_FEE = 869.00
ADD_CAR_DIS = .25

EX_LIA_FEE = 130.00
GLASS_FEE = 86.00
LOAN_CAR_FEE = 58.00

HST_RATE = .15
MON_PROC_FEE = 39.99
CUR_DATE = DT.datetime.now()

PROV_TERR_LIST = [ "NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU" ]
PAY_TYPE_LIST = [ "Full", "Monthly", "Down Pay" ]


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    while True:
        FName = input("Enter the customers first name: ").title()

        if FName == "":
            print()
            print("   Data Entry Error - First name cannot be blank. ")
            print() 
        else:
            break

    while True:
        LName = input("Enter the customers last name: ").title()

        if LName == "":
            print()
            print("   Data Entry Error - Last name cannot be blank. ")
            print()
        else:
            break

    while True:
        StAdd = input("Enter the customers street address: ").title()

        if StAdd == "":
            print()
            print("   Data Entry Error - Street address cannot be blank. ")
            print() 
        else:
            break

    while True:
        City = input("Enter the customers city: ").title()

        if City == "":
            print()
            print("   Data Entry Error - City cannot be blank. ")
            print() 
        else:
            break

    while True:
        Prov = input("Enter the customers province (XX): ").upper()
        
        if Prov == "":
            print()
            print("   Data Entry Error - Province cannot be blank. ")
            print() 
        elif len(Prov) != 2:
            print()
            print("   Data Entry Error - province must contain only 2 characters")
            print()
        elif Prov not in PROV_TERR_LIST:
            print()
            print("   Data Entry Error - Invalid Province/Territory")
            print()
        else:
            break

    while True:
        PostCode = input("Enter the customers postal code: ").upper()

        if PostCode == "":
            print()
            print("   Data Entry Error - Postal code cannot be blank. ")
            print() 
        else:
            break

    while True:
        PhoneNum = input("Enter the customers phone number: ")

        if PhoneNum == "":
            print()
            print("   Data Entry Error - Phone number cannot be blank. ")
            print() 
        else:
            break

    while True:
        NumCars = input("Enter the number of cars being insured: ")
        NumCars = int(NumCars)

        if NumCars == "":
            print()
            print("   Data Entry Error - Number of cars cannot be blank. ")
            print() 
        else:
            break

    while True:
        ExtraLia = input("Would the customer like extra liability up to $1,000,000 (Y/N): ").upper()

        if ExtraLia == "":
            print()
            print("   Data Entry Error - Extra liability cannot be blank. ")
            print() 
        else:
            break

    while True:
        GlassCov = input("Would the customer like optional glass coverage (Y/N): ").upper()

        if GlassCov == "":
            print()
            print("   Data Entry Error - Glass coverage cannot be blank. ")
            print() 
        else:
            break
    
    while True:
        LoanCar = input("Would the customer like an optional loaner car (Y/N): ").upper()

        if LoanCar == "":
            print()
            print("   Data Entry Error - Loaner car coverage cannot be blank. ")
            print() 
        else:
            break

    while True:
        PayType = input("What type of payment would the customer like to make (Full, Monthly or Down Pay): ").title()

        if PayType == "":
            print()
            print("   Data Entry Error - Payment type cannot be blank. ")
            print()
        elif PayType not in PAY_TYPE_LIST:
            print()
            print("   Data Entry Error - Invalid Payment Type")
            print()
        elif PayType == "Down Pay":
            print()
            DownPay = input("Enter the amount of the down payment: ")
            print()
            DownPay = float(DownPay)
            break
        else:
            break



    #Perform required calculations.



    # Display results



    # Write the values to a data file for storage.

    Continue = input("Do you want to process another claim (Y/N): ").upper() #would normally validate
    if Continue == "N":
        break


# Any housekeeping duties at the end of the program.