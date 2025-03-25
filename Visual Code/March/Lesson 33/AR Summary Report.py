# Description:AR Summary Report based on the data in the customer.dat file
# Author: Mo and Class
# Date(s): Mar 25/25


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
PAY_RATE = .10
CUR_DATE = datetime.datetime.now()


# Define program functions.



# Main report processing starts here.


# Generate report headings.
print()

print(f"                      WIDGITS INCORPORATED")
print()
print(f"       ACCOUNTS REVEIVABLE SUMMARY REPORT AS OF {FV.FDateS(CUR_DATE):<10s}")#dont have to align date where ther eis nothing after and will always be 10 characters
print(f" ACCOUNT       CUSTOMER          BALANCE    CREDIT     MINIMUM")
print(f" NUMBER          NAME              DUE     REMAINING   PAYMENT")
print(f"==============================================================")

# Initialize counters and accumulators.
CustCtr = 0
BalDueAcc = 0
MinPayAcc = 0

# Open the data file. Places the cursor at the start of the first record.
f = open("Customers.dat", "r")

# Process each line (record) in the file in a loop.
for CustRecord in f:

    # The following line reads the first record in the file and creates a list.
    CustLst = CustRecord.split(",")
    
    # Now grab the values from the list and assign to variables.
    # You may not need all the fields.
    CustNum = CustLst[0].strip()
    CustName = CustLst[1].strip()
    BalDue = float(CustLst[5].strip())
    CredLim = CustLst[6].strip()
    CredLim = float(CredLim)


    # Perform required calculations.
    CredRem = CredLim - BalDue
    
    if BalDue <= CredLim:
        MinPay = BalDue * PAY_RATE
    else:
        MinPay = (BalDue * PAY_RATE) + (BalDue - CredLim)
    
    '''
    OR
    MinPay = BalDue * PAY_RATE
    if BalDue > CredLim:
        MinPay += (BalDue - CredLim)
    '''

    # Display the detail line.
    print(f" {CustNum:<5s}   {CustName:<20s}  {FV.FDollar2(BalDue):>9s}  {FV.FDollar2(CredRem):>9s}  {FV.FDollar2(MinPay):>9s}")
    
    
    # Update counters and accumulators.
    CustCtr += 1
    BalDueAcc += BalDue
    MinPayAcc += MinPay


# Close the file.
f.close()

# Print summary data - counters and accumulators.
print(f"==============================================================")
print(f" Customers listed: {CustCtr:>3d}        {FV.FDollar2(BalDueAcc):>10s}            {FV.FDollar2(MinPayAcc):>10s}")
print()
print(f"                          END OF LISTING")
