# Description: Snuggly Company
# Author: Class and Mo
# Date(s): January 22/24
 
 
# Define required libraries.
 
 
 
# Define program constants.
SNUG_COST_LOW = 21.99
SNUG_COST_MED = 24.99
SNUG_COST_HIGH = 29.99

SHIP_COST_HIGH = 5.99
SHIP_COST_LOW = 3.99

HST_RATE = .15
CC_RATE = .03
 
# Define program functions.
 
 
 
# Main program starts here.
 
   
# Gather user inputs.
CustName = input("Enter the customers name: ")
StAdd = input("Enter the street address: ")
City = input("Enter the city: ")
Prov = input("Enter the province (XX): ").upper()
Postal = input("Enter the postal code (X0X0X0): ").upper()
Phone = input("Enter the phone number(000-000-0000): ")
CCNum = input("Enter the credit card number (0000-0000-0000-0000): ")
NumSnug = input("Enter the number of snugglys purchased: ")
NumSnug = int(NumSnug)


# Perform required calculations.
if NumSnug == 1:
    TotCostSnug = SNUG_COST_HIGH
elif NumSnug <= 10:
    TotCostSnug = SNUG_COST_MED * NumSnug
else: 
    TotCostSnug = SNUG_COST_LOW * NumSnug

if NumSnug < 6:
    TotCostShip = SHIP_COST_HIGH * NumSnug
else: 
    TotCostShip = SHIP_COST_LOW * NumSnug

SubTotal = TotCostSnug + TotCostShip
HST = SubTotal * HST_RATE
TotOrder = SubTotal + HST

SerCharge = TotOrder * CC_RATE

# Display results

print()
print(f"Cost of Snugglys:               {TotCostSnug}")
print(f"Cost of shipping:               {TotCostShip}")
print(f"Subtotal:                       {SubTotal}")
print(f"HST:                            {HST}")
print(f"Total order:                    {TotOrder}")
print(f"Credit Card service charge:     {SerCharge}")

  
# Write the values to a data file for storage.

 
 
# Any housekeeping duties at the end of the program.
#would still need to format the prints