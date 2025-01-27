# Comment like a pro

'''
if Criteria: #Test of a condition that returns true or false
    Statements(s) if the criteria is true.
    Jump out of the if statements and continue to the program
else:
    Statement(s) if the criteria is false
    Ignore the statements in the true block
    Again, jump out of the if when complete
'''
'''
Age = input("Enter the persons age: ")
Age = int(Age)

if Age >= 19:   #Other operators are >, <, >=, <=, ==, !==
    print("Allowed to vote.")
else:
    print("Too young to vote.")
'''

'''
PayRate = input("Enter the hourly pay rate: ")
PayRate = float(PayRate)
Hours = input("Enter the hours worked: ")
Hours = float(Hours)

if Hours <= 40: # The most common alternative is done first.
    GrossPay = PayRate * Hours
else:
    RegPay = PayRate * 40
    OTPay = (Hours - 40) * (PayRate * 1.5)
    GrossPay = RegPay + OTPay

print(GrossPay)
'''
'''
Status = input("Enter the marital status (S, M, W, O): ").upper()
#Status = Status.upper()
# The status will now always be upper case. Can do it on the same line or a seperate line

if Status == "S":
    print("Single")
elif Status == "M":
    print("Married")
elif Status == "W":
    print("Widowed")
else:
    print("Other")

# The elif is if there are more 2  criteria. The last one can be an else.
'''
'''
BalDue = input("Enter the balance due: ")
BalDue = float(BalDue)
CreditLim = input("Enter the credit limit: ")
CreditLim = float(CreditLim)

if BalDue <= CreditLim:
    PayDue = BalDue * .10
else: 
    PayDue =(BalDue * .10) + (BalDue - CreditLim)

print(PayDue)
'''
'''
#Question E

IntValue1 = input("Enter the first integer value: ")
IntValue1 = int(IntValue1)
IntValue2 = input("Enter the second integer value: ")
IntValue2 = int(IntValue2)
        
# Calculate sum, difference, product
Sum = IntValue1 + IntValue2
Diff = IntValue1 - IntValue2
Prod = IntValue1 * IntValue2

Quot = 0
QuotMsg = "" # An empty string is known as a null string.
if IntValue2 != 0:
    Quot = IntValue1 / IntValue2
else:
    QuotMsg = "Division by 0."

#Can only calculate the quotient if the IntValue2 is not 0
#If the if contains different variables in the true/false statements the variables must be intiialzed before the if.
#VAriable scope describes the visbility of a variable. Any variable used in a code block (ie: in an if) are only visible inside the code block. 
#That is why varibales need to be intiilized before the loop to make them visible to the rest of the program.. 

#Determine if a value is even or odd by divinding by 2 and checking. 
# A remainder is 1 it is odd, if the remainder id 0 it is even.
if IntValue1 % 2 == 0: # % is the mod operator and returns the remainder. 
     EvenOdd1 = "Even Number"
else:
    EvenOdd1 = "Odd Number"


if IntValue2 % 2 == 0:
     EvenOdd2 = "Even Number"
else:
    EvenOdd2 = "Odd Number"
    
print(f"Sum: {Sum}")
print(f"Difference: {Diff}")
print(f"Product: {Prod}")
if IntValue2 != 0:
    print(f"Quotient: {Quot}")
else: 
    print (f"Quotient: {QuotMsg}")
print(f"Even/Odd1: {EvenOdd1}")
print(f"Even/Odd2: {EvenOdd2}")
'''
'''
#Question 2

#Gather the Input
CustName = input("Enter the customer name: ")
CostParts = input("Enter the cost of parts: ")
CostParts = float(CostParts)
LaborHrs = input("Enter the number of labor hours: ")
LaborHrs = float(LaborHrs)

#Calculations
LaborCost = LaborHrs * 34.00
SubTotal = CostParts + LaborCost
Tax = SubTotal * .15
Total = SubTotal + Tax

#Display the results
print(f"Customer: {CustName}")
print(f"Parts: {CostParts}")
print(f"Labor Hours: {LaborHrs}")
print(f"Subtotal: {SubTotal}")
print(f"Labor Cost: {LaborCost}")
print(f"Tax: {Tax}")
if Total >= 500.00:
    Discount = Total * .10
    DiscountTotal = Total - Discount
    print(f"Discount: {Discount}")
    print(f"Total: {DiscountTotal}")
else: 
    print(f"Total: {Total}")
'''
'''
Maurice's Version
IntValue1 = input("Enter the first integer value: ")
IntValue1 = int(IntValue1)
IntValue2 = input("Enter the second integer value: ")
IntValue2 = int(IntValue2)
 
Sum = IntValue1 + IntValue2
Diff = IntValue1 - IntValue2
Prod = IntValue1 * IntValue2
 
# Can only calculate the quotient if IntValue2 is not 0.
 
# If the if contains different variables in the true/false statemets,
# the variables must be initialized before the if. Varaible Scope
# describes the visibility of a variable.  Any valriable used in a
# code block (ie: in an if) are only visible inside the code block.
# Varaibles need to be initialized before the loop to make them visible
# to the rest of the program.
 
Quot = 0
QuotMsg = "" # An empty string is known as a null string.
if IntValue2 != 0:
    Quot = IntValue1 / IntValue2
else:
    QuotMsg = "Division by 0."
 
# Determine if a value is even or odd by dividing by 2 and checking the remainder.
# A remainder is 1 it is odd, if the remainder is 0 it is even.
 
# I do not need to initialize since the value is being defined in both
# the if and the else code blocks.
 
if IntValue1 % 2 == 0: # % is the mod operator, and returns the remainder.
    EvenOdd1 = "Even Number"
else:
    EvenOdd1 = "Odd Number"
 
if IntValue2 % 2 == 0:
    EvenOdd2 = "Even Number"
else:
    EvenOdd2 = "Odd Number"
 
print(Sum)
print(Diff)
print(Prod)
if IntValue2 != 0:
    print(Quot)
else:
    print(QuotMsg)
print(EvenOdd1)
print(EvenOdd2)
'''
'''
Code for the first 4 exercises on Complex ifs.
 
# Description: asdfasdfasdfasfsdf
# Author: Maurice& SD 14
# Date(s): Jan 23, 2025 -
 
 
# Define required libraries.
 
 
 
# Define program constants.
 
 
 
# Define program functions.
 
 
# Examples of multiple if criteria using and/or.
# and - both criteria must be True.
# or - one or both of the criteria must be true.
 '''
'''
MarStat = input("Enter the marital status (S, M, W, D): ").upper()
Age = input("Enter the persons age: ")
Age = int(Age)
 
if MarStat == "M":
    MarDate = input("Enter the marriage date (YYYY-MM-DD): ")
elif (MarStat == "D" or MarStat == "W") and Age > 40:
    print("Better get into a relationship soon.")
 
if MarStat == "S":
    print("Single")
elif MarStat == "M":
    print("Married")
elif MarStat == "W":
    print("Widowed")
else:
    print("Divorced")

StudID = input("Entr the student ID (#######): ")
Grade = input("Enter the student grade (0-100): ")
Grade = int(Grade)
 
if Grade >= 90:
    LetterGrade = "A"
elif Grade >= 80 and Grade <= 89: # He Grade must fit in the range 80-89.
    LetterGrade = "B"
elif Grade >= 70 and Grade <= 79:
    LetterGrade = "C"
elif Grade >= 60 and Grade <= 69:
    LetterGrade = "D"
else:
    LetterGrade = "F"
 
print(LetterGrade)
'''
 
'''
BalDue = input("Eenter the customer balance due: ")
BalDue = float(BalDue)
CredLim = input("Enter the customer credit limit: ")
CredLim = float(CredLim)
 
if BalDue <= CredLim:
    PayDue = BalDue * .10
    Status = "OK"
else:
    PayDue = (BalDue * .10) + (BalDue - CredLim)
    Status = "OVER"
 
if BalDue > CredLim + 1000.00:
    Status = Status + " - CREDIT CHECK"
 
# When you want to add something to a value.  Make sure you specify the original value
# and what you want to add to it.
#     X = X + 10
#     Status = Status + " - CREDIT CHECK"
# Shortcut - use the += operator - adds to the original value and places the
# result back to the original varaible.
#     X += 10
#     Status += " - CREDIT CHECK"
# Also use -=, *=, and /=.
 
print(PayDue)
print(Status)
'''
'''
LoanAmt = input("Enter the loan amount: ")
LoanAmt = float(LoanAmt)
 
if LoanAmt < 25000.00:
    Dep = LoanAmt * .05
elif LoanAmt >= 25000.00 and LoanAmt <= 49999.00:
    Dep = 1250.00 + (LoanAmt - 25000.00) * .10
elif LoanAmt >= 50000.00 and LoanAmt <= 100000.00:
    Dep = 5000.00 + (LoanAmt - 50000.00) * .25
 
print(Dep)

 
 
# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.
 '''


