# Description: Lesson 12
# Author: Mo and Class 
# Date(s): January 23/2024
#Question 1: Marital Status
 
 

# Define required libraries.
 
 
 
# Define program constants.


 
# Define program functions.
 
 
#Examples of multiple if criteria using and/or

BalDue = input("Enter the customer balance due: ")
BalDue = float(BalDue)
CreditLim = input("Enter the customer credit limit: ")
CreditLim = float(CreditLim)

if BalDue <= CreditLim:
    PayDue = BalDue * .10
    Status = "OK"
else:
    PayDue = (BalDue * .10) + (BalDue - CreditLim)
    Status = "OVER"

if BalDue > CreditLim + 1000.00:
    Status = Status + " - CREDIT CHECK"

print(PayDue)
print(Status)

# Main program starts here.
 
   

# Gather user inputs.

 
 
# Perform required calculations.



# Display results



# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.