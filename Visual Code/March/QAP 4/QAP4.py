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
# See imported library FormatValues

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
        ProvTerr = input("Enter the customers province/territory (XX): ").upper()
        
        if ProvTerr == "":
            print()
            print("   Data Entry Error - Province/Territory cannot be blank. ")
            print()
        elif len(ProvTerr) != 2:
            print()
            print("   Data Entry Error - Province/Territory must contain only 2 characters")
            print()
        elif ProvTerr not in PROV_TERR_LIST:
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

    DownPay = 0
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

    ClaimNumbers = ["CLM-3981-2398", "CLM-6721-1421"]
    ClaimDates = ["2024-09-13", "2025-01-13"]
    ClaimAmounts = [2300, 5750]
    
    
    ClaimNum = input("Enter the claim number (CLM-####-####): ").upper()
    ClaimNumbers.append(ClaimNum)

    ClaimDate = input("Enter the claim date (YYYY-MM-DD): ")
    ClaimDate = DT.datetime.strptime(ClaimDate, "%Y-%m-%d")
    ClaimDates.append(ClaimDate)


    ClaimAmount = float(input("Enter the claim amount: "))
    ClaimAmounts.append(ClaimAmount)


    #Perform required calculations.

    InsPre, LiaCost, GlassCost, LoanCost, TotExtraCost, TotInsPre, HST, TotCost, MonPay = FV.GetInsCosts(
        NumCars, ExtraLia, GlassCov, LoanCar, DownPay, BASIC_PRE_FEE, ADD_CAR_DIS, EX_LIA_FEE, GLASS_FEE, LOAN_CAR_FEE, HST_RATE
    )
    
    PayDueDate = FV.GetPayDue(CUR_DATE)
    CustNameDsp = FName + " " + LName
    TopAddressDsp = StAdd + ", " + City
    BottomAddressDsp = ProvTerr + " " + PostCode
    
    # Display results

    print()
    print(f"         ONE STOP INSURANCE COMPANY")
    print(f"            CUSTOMER INVOICE")
    print()
    print(f"                                   Policy Number: {POL_NO:>4d}")
    print(f"Customer Information:              Invoice Date: {FV.FDateS(CUR_DATE)}")
    print(f"     {CustNameDsp:<25s}            Number of Cars Insured: {NumCars:>2d}")
    print(f"     {TopAddressDsp:<25s}          ---------------------------------------")
    print(f"     {BottomAddressDsp:<10s}       OPTIONAL COVERAGES")
    print(f"     {PhoneNum:<14s}               Extra Liability: {FV.FDollar2(LiaCost):>10s}")
    print(f"                                   Glass Coverage:  {FV.FDollar2(GlassCost):>10s}")
    print(f"                                   Loaner Car:      {FV.FDollar2(GlassCost):>10s}")
    print(f"----------------------------------------------------------------------------")
    print(f"                                   Insurance Premium:{FV.FDollar2(InsPre):>10s}")
    print(f"                                   Total Extra Coverages:{FV.FDollar2(TotExtraCost):>10s}")
    print(f"                                   HST:{FV.FDollar2(HST):>10s}")
    print(f"                                   Total:{FV.FDollar2(TotCost):>10s}")

    #print()
    #print(f"         ONE STOP INSURANCE COMPANY")
    #print(f"            CUSTOMER INVOICE")
    #print(f"One Stop Insurance Company                   Policy Number:             {POL_NO:>4d}")
    #print(f"Customer Invoice                             Invoice Date:        {FV.FDateS(CUR_DATE)}")
    #print(f"                                             First Payment Date:   {FV.FDateS(PayDueDate)}")
    #print(f"--------------------------------------------------------------------------------")
    #print(f"Customer Information:                        {CustNameDsp:<25s}")
    #print(f"                                             {TopAddressDsp:<25s}")
    #print(f"                                             {BottomAddressDsp:<10s}")
    #print(f"                                             {PhoneNum:<14s}")
    #print(f"--------------------------------------------------------------------------------")
    #print(f"Number of Cars Insured: {NumCars:>2d}     Extra Liability Charge: {FV.FDollar2(LiaCost):>10s}")
    #print(f"Payment Type: {PayType:<8s}               Glass Coverage Charge:  {FV.FDollar2(GlassCost):>10s}")
    
    #if PayType == "Down Pay":
        #print(f"Down Payment: {FV.FDollar2(DownPay):>10s}  Loaner Car Charge:      {FV.FDollar2(GlassCost):>10s}")
    #else:
        #print(f"                                          Loaner Car Charge:      {FV.FDollar2(GlassCost):>10s}")
    
    #print(f"Insurance Premium:   ")
    

    # Write the values to a data file for storage.

    Continue = input("Do you want to process another claim (Y/N): ").upper()
    if Continue == "N":
        break

# (Insurance Premium, Extra Liability Cost, Glass Coverage Cost, Loaner Car Cost, Total Extra Costs, Total Insurance Premium, HST, Total Cost & Monthly Payments)
# Any housekeeping duties at the end of the program.