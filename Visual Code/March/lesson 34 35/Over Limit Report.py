# Description:Over Credit Limit Report
# Author: Mo and Class
# Date(s): Mar 27/25


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
CUR_DATE = datetime.datetime.now()


# Define program functions.



# Main report processing starts here.


# Generate report headings.
print(f"COMPANY NAME")
print(f"OVER LIMIT REPORT AS OF {FV.FDateS(CUR_DATE):<10s}")
print()
print(f"CUSTOMER      CUSTOMER            PHONE        CREDIT    AMOUNT     NEXT      PAYMENT")
print(f" NUMBER         NAME              NUMBER       LIMIT      OVER    PAY DATE      DUE")
print(f"======================================================================================")

# Initialize counters and accumulators.
CustCtr = 0
PayDueAcc = 0


# Open the data file. Places the cursor at the start of the first record.
f = open("CustExtra.dat", "r")

# Process each line (record) in the file in a loop.
for XRecord in f:

    # The following line reads the first record in the file and creates a list.
    XLst = XRecord.split(",")
    
    # Now grab the values from the list and assign to variables.
    # You may not need all the fields.
    CustNum = XLst[0].strip()
    CustName = XLst[1].strip()
    PhoneNum = XLst[2].strip()
    BalDue = float(XLst[3].strip())
    CredLim = float(XLst[4].strip())
    NextPayDate = XLst[9].strip() #any field read is a string, so alwsys remember to parse numbers and dates
    NextPayDate = datetime.datetime.strptime(NextPayDate, "%Y-%m-%d")
    
    #if for the exception generally before the start of the calculations
    if BalDue > CredLim:

        # Perform required calculations.
        AmtOver = BalDue - CredLim
        PayDue = (CredLim * .05) + AmtOver

        # Display the detail line.
        print(f" {CustNum:<6s} {CustName:<20s} {PhoneNum:<14s}  {FV.FDollar2(CredLim):>9s} {FV.FDollar2(AmtOver):>9s}  {FV.FDateS(NextPayDate):<10s}  {FV.FDollar2(PayDue):>9s}")


        # Update counters and accumulators.
        CustCtr += 1
        PayDueAcc += PayDue


# Close the file.
f.close()

# Print summary data - counters and accumulators.
print(f"======================================================================================")
print(f"Total customer over limit: {CustCtr:>3d}                                                {FV.FDollar2(PayDueAcc):>10s}")

