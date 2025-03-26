# Description: Payment due report for customers using the Customers.dat file.
# Author: Maurice & SD 14
# Date(s): Mar 26/25 -
 
 
# Define required libraries.
import datetime
import FormatValues as FV
 
 
# Define program constants.
CUR_DATE = datetime.datetime.now()
PAY_RATE = .10
 
# Define program functions.
 
 
 
# Main report processing starts here.
 
 
# Generate report headings.
print()
print(f"                            WIDGITS INCORPORATED")
print()
print(f"                     PAYMENT DUE REPORT AS OF {FV.FDateS(CUR_DATE):<10s}")
print()
print(f" ACCOUNT      CUSTOMER           BALANCE    MINIMUM    NEXT DUE      PHONE")
print(f" NUMBER         NAME               DUE      PAYMENT      DATE        NUMBER")
print(f"===========================================================================")
 
# Initialize counters and accumulators.
CustCtr = 0
BalDueAcc = 0
MinPayAcc = 0
OverCtr = 0
 
# Open the data file. Places the cursor at the start of the first record.
f = open("Customers.dat", "r")
 
# Process each line (record) in the file in a loop.
for XRecord in f:
 
    # The following line reads the first record in the file and creates a list.
    XLst = XRecord.split(",")
   
    # Now grab the values from the list and assign to variables.
    # You may not need all the fields.
    CustNum = int(XLst[0].strip())
    CustName = XLst[1].strip()
    BalDue = float(XLst[5].strip())
    CredLim = float(XLst[6].strip())
    PhoneNum = XLst[4].strip()
 
    # For an exception report, place an if around the calcs and prints.  
    # Only the records that match the criteria will be printed.
    if BalDue > CredLim:
        # Perform required calculations.
        if BalDue <= CredLim:
            MinPay = BalDue * PAY_RATE
        else:
            MinPay = (BalDue * PAY_RATE) + (BalDue - CredLim)
 
        if BalDue <= 200.00:
            NextPayDate = CUR_DATE + datetime.timedelta(days=60)
        elif BalDue > 200.00 and BalDue <= CredLim:
            CurDay = CUR_DATE.day
            CurMonth = CUR_DATE.month
            CurYear = CUR_DATE.year
 
            PayDay = 1
            PayMonth = CurMonth + 1
            if CurDay > 25:
                PayMonth += 1
            PayYear = CurYear
 
            if PayMonth > 12:
                PayMonth -= 12
                PayYear += 1
            NextPayDate = datetime.datetime(PayYear, PayMonth, PayDay)
        else:
            NextPayDate = CUR_DATE + datetime.timedelta(weeks=2)
       
 
        if BalDue <= CredLim:
            PhoneNum = ""
       
        # Display the detail line.
        print(f" {CustNum:>5d}   {CustName:<20s}   {FV.FDollar2(BalDue):>9s}   {FV.FDollar2(MinPay):>9s}   {FV.FDateM(NextPayDate):<9s}  {PhoneNum:>8s}")
       
        # Update counters and accumulators.
        CustCtr += 1
        BalDueAcc += BalDue
        MinPayAcc += MinPay
        if BalDue > CredLim:
            OverCtr += 1
 
 
# Close the file.
f.close()
 
# Print summary data - counters and accumulators.
print(f"===========================================================================")
print(f" Customers lsited: {CustCtr:>3d}         {FV.FDollar2(BalDueAcc):>10s}  {FV.FDollar2(MinPayAcc):>10s}        Over limit: {OverCtr:>2d}")
print()
print(f"                               END OF LISTING")