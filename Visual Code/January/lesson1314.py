#Code for the first few problems on the Loop Lesson Plan.  Complete the Temp and Loan programs for next day.
 
'''print(1)
print(2)
print(3)
# and so on.
 
# for loop - if you know exactly how many iterations are needed.
for Num in range(1, 11):
    Square = Num ** 2 # the ** is used to raise to the power of.
    Cube = Num ** 3
    print(Num, Square, Cube)
 
# When it reaches the top value - the program jumps out of the loop.
# If you want to use that last value, set it to the top value + 1.
 
# Now create a loop with a while.  This loop is executed as long as a criteria is met.
# Always initialize the starting value before the loop.
Num = 1
while Num <= 10:
    print(Num)
    # In a whie loop, you need to increment the value inside the loop.
    Num += 1
 
 
LoopCtr = input("Enter a number between 1 and 10: ")
LoopCtr = int(LoopCtr)
 
for Graph in range(1, LoopCtr+1):
    # How do I get this to print on one line.  Print statements by defualt will put
    # a line break at the end.
    print("*", end="") # Keeps the print on the same line.
 
# For multiple lines in the graph, need multiple inputs and multiple loops.
 
 
# When printing a table, the headings are printed before the loop, the values are
# calculated and printed inside the loop, the line at the end is printed after the loop.
 
print(f" Celsius   Fahrenheit")
print(f" --------------------")
 
for CelTemp in range(-20, 31):
 
    FahTemp = (9 / 5 * CelTemp) + 32
    FahTempDsp = "{:.1f}".format(FahTemp)
    print(f" {CelTemp:>3d}          {FahTempDsp:>4s}")
   
print(f" -------------------------")
'''
'''
print(f" Celsius Fahrenheit Kelvin")
print(f" -------------------------------------------------")
 
for CelTemp in range(-100, 100):
 
    FahTemp = (9 / 5 * CelTemp) + 32
    KelTemp = CelTemp + 273.15
    FahTempDsp = "{:.1f}".format(FahTemp)
    print(f" {CelTemp:>3d}          {FahTempDsp:>4s}")
   
print(f" --------------------")
'''
'''
print("Temperature Conversion Chart")
print()
print("Celsius Fahrenheit Kelvin         Message")
print("-------------------------------------------------")

for CelTemp in range(-100, 100):
    #if you want to go by increments other than 1 you can add ,5 after the numbers. (-100, 100, 5), would go by increments of 5:
    FahTemp = (9 / 5 * CelTemp) + 32
    KelTemp = CelTemp + 273.15

    Msg = ""
    if CelTemp == -90:
        Msg = "Lowest Recorded Temperature"
    elif CelTemp == 0:
        Msg = "Freezing Point of Water"
    elif CelTemp == 20:
        Msg = "Average Room Temperature"
    elif CelTemp == 100:
        Msg = "Boiling Point of Water"
    #else:
    #Msg = ""

    FahTempDsp = "{:.1f}".format(FahTemp)
    KelTempDsp = "{:.1f}".format(KelTemp)
    print(f" {CelTemp:>4d}     {FahTempDsp:>6s}     {KelTempDsp:>6s}  {Msg:<22s}")

print("-------------------------------------------------")
'''

'''
LoanAmt = input("Enter the loan amount: ")
LoanAmt = float(LoanAmt)
Reason = input("Enter the reason for the loan: ")

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
'''

while True:
    # Gather user inputs
    CusFirName = input("Enter the customer's first name (or type 'END' to exit): ")
    if CusFirName.upper() == "END":
        break
    CusLasName = input("Enter the customer's last name: ")
    VacationDest = input("Enter the vacation destination: ")
    DepartureDate = input("Enter the departure date (YYYY-MM-DD): ")
    NumPersons = int(input("Enter the number of persons: "))
    CostPerWeek = float(input("Enter the cost per week: "))
    NumWeeks = int(input("Enter the number of weeks: "))
    ConnectorFlight = input("Does the customer need a connector flight to Toronto (Y or N): ").upper()

    # Calculate vacation cost
    VacationCost = NumPersons * CostPerWeek * NumWeeks
    ConnectorFlightCost = 350.00 * NumPersons if ConnectorFlight == 'Y' else 0.00
    Subtotal = VacationCost + ConnectorFlightCost
    SalesTax = Subtotal * 0.13
    TotalCost = Subtotal + SalesTax

    # Apply discount if applicable
    Discount = 0.00
    if TotalCost > 2000.00 or NumWeeks > 2:
        Discount = VacationCost * 0.05
        TotalCost -= Discount

    # Display the gathered information
    print("\nCustomer Vacation Details")
    print("-------------------------")
    print(f"Customer Name:           {CusFirName} {CusLasName}")
    print(f"Vacation Destination:    {VacationDest}")
    print(f"Departure Date:          {DepartureDate}")
    print(f"Number of Persons:       {NumPersons}")
    print(f"Cost Per Week:           ${CostPerWeek:,.2f}")
    print(f"Number of Weeks:         {NumWeeks}")
    print(f"Connector Flight to Toronto: {ConnectorFlight}")
    print(f"Connector Flight Cost:   ${ConnectorFlightCost:,.2f}")

    # Display calculated results
    print("\nCost Breakdown")
    print("--------------")
    print(f"Vacation Cost:           ${VacationCost:,.2f}")
    print(f"Subtotal:                ${Subtotal:,.2f}")
    print(f"Sales Tax (13%):         ${SalesTax:,.2f}")
    if Discount > 0:
        print(f"Discount (5%):           -${Discount:,.2f}")
    print(f"Total Cost:              ${TotalCost:,.2f}")

    # Calculate and display payment options
    print("\nPayment Options")
    print("---------------------------")
    print(f"# Payments:          ${TotalCost:,.2f}      Monthly Payments:   ")

    for months in [3, 6, 9, 12, 15]:
        Interest = TotalCost * 0.065 * (months / 12)
        TotalWithInterest = TotalCost + Interest
        MonthlyPayment = TotalWithInterest / months
        print(f"{months}              {MonthlyPayment:,.2f}")

    # Ask if the user wants to continue
    continue_choice = input("\nWould you like to enter another customer? (Y/N): ").upper()
    if continue_choice != 'Y':
        break