# Comment like a pro.
 
# After the IPO, develop a set of test data.
'''
EmpName = "John Smith"
HrsWorked = 40
TotSales = 4000.00
AssItems = 50

RegPay = 40 * 17.50 = 700
SalesComm = 4000.00 * .06 = 240.00
:
:
# Now when you run the program to test it, you have numbers to reference.
'''

# Define program constants.
HOURLY_PAY_RATE = 17.50
SALES_COMM_RATE = .06 # 6%
ASS_COMM_RATE = .45 # 45 cents
INC_TAX_RATE = .17
CPP_RATE = .0495
EI_RATE = .016
UNION_RATE = 12.00 # Flat rate fee
MED_BEN_RATE = .05

#After you check and everything is good you can delete the prints below. These are only typed out to check them. 
print(HOURLY_PAY_RATE)
print(SALES_COMM_RATE)
print(UNION_RATE)
print(MED_BEN_RATE)


# Gather user input.
EmpName = "John Smith" #input("Enter the employee name: ")
HrsWorked = 40 #input("Enter the number of hours worked (20 - 60): ")
HrsWorked = int(HrsWorked)
TotSales = 4000.00 #input("Enter the total sales for the period (1000.00 - 7000.00): ")
TotSales = float(TotSales)
AssItems = 50 #input("Enter the number of items assembled (20 - 100): ")
AssItems = int(AssItems)

#After the inputs, again, print out the values and then delete with accurate.
print(EmpName)
print(HrsWorked)
print(TotSales)
print(AssItems)
#When accurate, ass the values to the input and comment out the input() statement.
#Now you do not have to input eveyrytime you run. the test data will take over.
#Once the program is complete, reset the input statements.

# Perform required calculations.
RegPay = HrsWorked * HOURLY_PAY_RATE
SalesComm = TotSales * SALES_COMM_RATE

#After a couple of calcualtions, print the results to check. 
print(RegPay)
print(SalesComm)
#After testing, delete the prints.

AssComm = AssItems * ASS_COMM_RATE
TotComm = SalesComm + AssComm
GrossPay = RegPay + TotComm
#After a couple of calculations, print the results to check. 
print(AssComm)
print(TotComm)
print(GrossPay)
#After testing, delete the prints.
 
IncTax = GrossPay * INC_TAX_RATE
CPP = GrossPay * CPP_RATE
EI = GrossPay * EI_RATE
UnionDues = UNION_RATE
MedBen = GrossPay * MED_BEN_RATE
TotDed = IncTax + CPP + EI + UnionDues + MedBen
 
NetPay = GrossPay - TotDed

# All input and output values have been verified. Now I just concentrate on printing results using the printer sapcing chart as described. 

# Display program results.
print()
print(f"   ABC COMPANY")
print(f"   Employee Weekly Payroll Summary")
print()
print(f"   Employee name: {EmpName:<20s}")
print()
 
HOURLY_PAY_RATEDsp = "${:.2f}".format(HOURLY_PAY_RATE)
print(f"   Hours worked: {HrsWorked:>2d}     Pay rate: {HOURLY_PAY_RATEDsp:>6s}")
print()
 
SALES_COMM_RATEDsp = "{:.0%}".format(SALES_COMM_RATE)
ASS_COMM_RATEDsp = "{:.2f}".format(ASS_COMM_RATE)
print(f"   Commission rates:    On sales:    {SALES_COMM_RATEDsp:>3s}   On assemblies: {ASS_COMM_RATEDsp:>4s}")
# When you print a value as a float that is just the decimal, it adds a 0 before the decimal on the output.
print()
 
RegPayDsp = "${:.2f}".format(RegPay)
print(f"        Regular pay:                        {RegPayDsp:>9s}")
print()
 
SalesCommDsp = "${:.2f}".format(SalesComm)
print(f"           Sales commission:     {SalesCommDsp:>9s}")
 
AssCommDsp = "${:.2f}".format(AssComm)
print(f"           Assembly commission:  {AssCommDsp:>9s}")
print(f"                                 ---------  ---------")
 
TotCommDsp = "${:.2f}".format(TotComm)
print(f"        Total commission:                   {TotCommDsp:>9s}")
print(f"                                            ---------")
 
GrossPayDsp = "${:.2f}".format(GrossPay)
print(f"        Gross pay:                          {GrossPayDsp:>9s}")

#When the program is complete:
    #Delete the test data
    #Remove the values on the inputs and resest the input() statements. 
    #Remove any print() statements that you used for testing. 

    #After the inputs, again, print out the values and then delete with accurate.
