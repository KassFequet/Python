# Description: Invoice Analysis
# Author: Class
# Date(s): Feb 10/25


# Define required libraries.
import datetime



# Define program constants.
CUR_DATE = datetime.datetime.now()
DIS_RATE = .02


# Define program functions.



# Main program starts here.
while True:

    # Gather user inputs.
    #When entering a date - validate like a numeric value.
    while True:
        try:
            InvDate = input("Enter the invoice date (YYYY-MM-DD): ")
            InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
        except:
            print(" Error - date is invalid - use YYYY-MM-DD format")
        else:
            #validate to ensure it i not a future date
            if InvDate > CUR_DATE:
                print("  Error - cannot enter a date in the future")
            else:
                break


    while True:
        try:
            InvAmt = input("Emter the invoice amount: ")
            InvAmt = float(InvAmt)
        except:
            print("Error - Invoice amount must be a valid number")
        else: 
            break

    # Perform required calculations.
    #The discount date is 10 dats from the Invoice date.
    DisDate = InvDate + datetime.timedelta(days=10)

    #The discount amount is 2% off the original imvoice amount.
    DisAmt = InvAmt - (InvAmt * DIS_RATE) # = InvAmt * .98

    #The due date is 30 dats from the invoice date.
    DueDate = InvDate + datetime.timedelta(days=30)

    #The age of the invoice is the time from the current date
    InvAge = (CUR_DATE - InvDate).days





    # Display results
    print()
    print(f"ABC Company")
    print(f"Invoice Analysis Program")
    print()
    InvAmtDsp = "${:,.2f}".format(InvAmt)
    print(f"   Original Invoice Amount:       {InvAmtDsp:>10s}")

    InvDateDsp = datetime.datetime.strftime(InvDate, "%m-%b-%y")
    print(f"   Original Invoice Date:         {InvDateDsp:>10s}")

    print()
    DueDateDsp = datetime.datetime.strftime(DueDate, "%m-%b-%y")
    print(f"   Discount Date:                 {DueDateDsp:>10s}")

    DisAmtDsp = "${:,.2f}".format(DisAmt)
    print(f"   Discount Amount:                {DisAmtDsp:>10s}")

    print()
    print("    Invoice Age :                   {InvAge:>3d} days. ")




    # Write the values to a data file for storage.



    while True:
        Continue = input("Would you like to analyze another invoice:")

        if Continue != "Y" and Continue != "N":
            print("Error - Continue must be option Y or N only")
        else:
            break

    if Continue == "N":
        break #Jump out of the main loop and do the housekeeping 
    
    # Add a break statement to avoid an infinite loop







#Any housekeeping duties at the end of the program.