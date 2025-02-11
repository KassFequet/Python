# Description: Template 
# Author: 
# Date(s): 
 
 
# Define required libraries.
 
 
 
# Define program constants.

 

# Define program functions.

 
 
# Main program starts here.
#The loop to repeat the program is placed around the IPO, Libraries, constants and functions are only processed once and are not placed in the loop. Even the housekeeping at the end would only be executed when the user jumps out of the loop. Use a while true since you do not know how many times the user needs to repeat the program.  
   
while True:

    # Gather user inputs.
    print()
    #one way to exit the loop (ie end the program) is to enter a sentinal value. A value that will force the program to end.
    LoanAmt = input("Enter the loan amount: ")
    LoanAmt = float(LoanAmt)
    if LoanAmt == 0:
        break #jumps out of the current loop

    Reason = input("Enter the reason for the loan(0 to quit): ")
    print()
    
    
    # Perform required calculations.
    print()
    LoanAmtDsp = "${:,.2f}".format(LoanAmt)
    print(f"Loan Options for 10 Years on {LoanAmtDsp:>9s}")
    print()
    print(f"   Years   Interest   Total Amt   Mon Payment")
    print(f"   ------------------------------------------")

    for Years in range(1,11):
        Interest = LoanAmt * .065 * Years
        TotAmt = LoanAmt + Interest
        Months = Years * 12
        MonPay = TotAmt / Months

        InterestDsp = "${:,.2f}".format(Interest)
        TotAmtDsp = "${:,.2f}".format(TotAmt)
        MonPayDsp = "${:,.2f}".format(MonPay)
        print(f" {Years:>2d}    {InterestDsp:>9s}    {TotAmtDsp:>9s}    {MonPayDsp:>9s}")

    print(f"   ------------------------------------------")
    print()



    # Display results



    # Write the values to a data file for storage
    #prompt the user to continue or end the program. this is done after all processing is done and generally the last step in a loop.

    print()
    Continue = input("Do you want to process another loan? (Y / N): ").upper()
    if Continue =="N":
        break
 
 
# Any housekeeping duties at the end of the program.
print()
print(f"  --------------------------------------------------")
print(f"                 Have a nice day!")
print(f"  --------------------------------------------------")
print()