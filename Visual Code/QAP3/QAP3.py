# Main program starts here.# Description: QAP #3 - Honest Harry Car Sales
# Author: Kassaundra Fequet
# Date(s): February 7/25 -

# Define required libraries.
import datetime
import random
import math

# Define program constants.
MAX_SELL_PRICE = 50000.00
CUR_DATE = datetime.datetime.now()
LOW_LIC_FEE = 75.00
HIGH_LIC_FEE = 165.00
LOW_TRAN_FEE = .01
HIGH_TRAN_FEE = .026
HST_RATE = .15
FINANCE_FEE = 39.99

# Main program starts here.
allowed_num = set("1234567890")
allowed_upper_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_upper_lower_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

while True:
    # Gather user inputs.
    while True:
        FirstName = input("Enter the customers first name (or type 'END' to exit): ").title()
        if FirstName == "":
            print("\n   Data Entry Error - First name must be entered\n")
        else:
            break

    if FirstName.upper() == "END":
        break

    while True:
        LastName = input("Enter the customers last name: ").title()
        if LastName == "":
            print("\n   Data Entry Error - Last name must be entered\n")
        else:
            break

    while True:
        PhoneNum = input("Enter the customer phone number (0000000000): ")
        if PhoneNum == "":
            print("\n   Data Entry Error - Phone number must be entered.\n")
        elif len(PhoneNum) != 10:
            print("\n   Data Entry Error - Phone number must contain 10 digits only\n")
        elif not PhoneNum.isdigit():
            print("\n   Data Entry Error - Phone number contains invalid characters\n")
        else:
            break

    while True:
        PlateNum = input("Enter the plate number (XXX000): ").upper()
        if PlateNum == "":
            print("\n   Data Entry Error - Plate number must be entered\n")
        elif len(PlateNum) != 6:
            print("\n   Data Entry Error - Plate number must be 6 characters only\n")
        elif not set(PlateNum[0:3]).issubset(allowed_upper_lower_char):
            print("\n   Data Entry Error - Plate number must start with 3 letters\n")
        elif not PlateNum[3:6].isdigit():
            print("\n   Data Entry Error - Plate number must end with 3 numbers\n")
        else:
            break

    while True:
        CarMake = input("Enter the car make: ")
        if CarMake == "":
            print("\n   Data Entry Error - Car make must be entered\n")
        elif not set(CarMake).issubset(allowed_upper_lower_char):
            print("\n   Data Entry Error - Car make must be letters\n")
        elif len(CarMake) > 13:
            print("\n   Data Entry Error - Car make cannot exceed 13 characters\n")
        else:
            break

    while True:
        CarModel = input("Enter the car model: ")
        if CarModel == "":
            print("\n   Data Entry Error - Car model must be entered\n")
        elif len(CarModel) > 10:
            print("\n   Data Entry Error - Car model cannot exceed 10 characters\n")
        else:
            break

    while True:
        CarYear = input("Enter the car year: ")
        if CarYear == "":
            print("\n   Data Entry Error - Car year must be entered\n")
        elif len(CarYear) != 4:
            print("\n   Data Entry Error - Car year must be 4 digits only\n")
        elif not CarYear.isdigit():
            print("\n   Data Entry Error - Car year must be numbers\n")
        else:
            break

    while True:
        SellPrice = input("Enter the selling price: ")
        if SellPrice == "":
            print("\n   Data Entry Error - Sell price must be entered\n")
        elif not SellPrice.isdigit():
            print("\n   Data Entry Error - Sell price must be numbers\n")
        else:
            SellPrice = float(SellPrice)
            if SellPrice > MAX_SELL_PRICE:
                print("\n   Data Entry Error - Sell price cannot exceed $50,000.00\n")
            else:
                break

    while True:
        TradeAmt = input("Enter the amount of the trade in: ")
        if TradeAmt == "":
            print("\n   Data Entry Error - Trade amount must be entered\n")
        elif not TradeAmt.isdigit():
            print("\n   Data Entry Error - Trade amount must be numbers\n")
        else:
            TradeAmt = float(TradeAmt)
            if TradeAmt > SellPrice:
                print("\n   Data Entry Error - Trade amount cannot exceed the sell price\n")
            else:
                break

    while True:
        SalesName = input("Enter the salespersons name: ")
        if SalesName == "":
            print("\n   Data Entry Error - Salespersons name must be entered\n")
        else:
            break

    # Perform required calculations.
    PriAftTrade = SellPrice - TradeAmt

    if SellPrice <= 15000:
        LicenseFee = LOW_LIC_FEE
    else:
        LicenseFee = HIGH_LIC_FEE

    if SellPrice < 20000:
        TransFee = LOW_TRAN_FEE * SellPrice
    else:
        TransFee = HIGH_TRAN_FEE * SellPrice

    Subtotal = PriAftTrade + LicenseFee + TransFee
    HST = HST_RATE * Subtotal
    TotSalePrice = Subtotal + HST

    # Calculations to prepare for printing format.
    FInitial = FirstName[0]
    LInitial = LastName[0]
    FLInitial = FInitial + LInitial
    FullName = FInitial + ". " + LastName
    PhoneNumDsp = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    CarDetails = CarYear + " " + CarMake + " " + CarModel
    PlateNumEnd = PlateNum[3:6]
    PhoneNumEnd = PhoneNum[6:10]
    ReceiptID = FLInitial + "-" + PlateNumEnd + "-" + PhoneNumEnd

    # Display results
    print()
    InvDateDsp = (CUR_DATE.strftime("%B %d, %Y"))
    print(f"Honest Harry Car Sales                           Invoice Date: {InvDateDsp:<20s}")
    print(f"Used Car Sales and Receipt                       Receipt No:         {ReceiptID:<11s}")
    print()
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    print(f"                                              Sale price:            {SellPriceDsp:>10s}")
    TradeAmtDsp = "${:,.2f}".format(TradeAmt)
    print(f"Sold to:                                      Trade Allowance:   {TradeAmtDsp:>10s}")
    print(f"                                              ----------------------------------")
    PriAftTradeDsp = "${:,.2f}".format(PriAftTrade)
    print(f"      {FullName:<30s} Price after Trade: {PriAftTradeDsp:>10s}")
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    print(f"      {PhoneNumDsp:<14s}                      License Fee:        {LicenseFeeDsp:>10s}")
    TransFeeDsp = "${:,.2f}".format(TransFee)
    print(f"                                              Transfer fee:           {TransFeeDsp:>10s}")
    print(f"                                          ----------------------------------")
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    print(f"Car Details:                                  Subtotal: {SubtotalDsp:>10s}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f"                                              HST: {HSTDsp:>10s}")
    print(f"    {CarDetails:<30s}                        ----------------------------------")
    TotSalePriceDsp = "${:,.2f}".format(TotSalePrice)
    print(f"                                             Total sales price: {TotSalePriceDsp:>10s}")
    print()
    print(f"-----------------------------------------------------------------------")
    print()

    # Print the header once
    print(f"                          Financing     Total        Monthly")
    print(f"# Years     # Payments       Fee        Price        Payment")
    print(f"------------------------------------------------------------")

    for Years in range(1, 5):
        Months = Years * 12
        FinFee = FINANCE_FEE * Years
        TotPrice = TotSalePrice + FinFee
        MonPay = TotPrice / Months

        FinFeeDsp = "${:,.2f}".format(FinFee)
        TotPriceDsp = "${:,.2f}".format(TotPrice)
        MonPayDsp = "${:,.2f}".format(MonPay)

        # Print each year's details on a new line
        print(f"  {Years}   {Months}    {FinFeeDsp:>7s}   {TotPriceDsp:>10s}   {MonPayDsp:>10s}")

    # Write the values to a data file for storage.
    # (This part is left as a placeholder for actual file writing code)
