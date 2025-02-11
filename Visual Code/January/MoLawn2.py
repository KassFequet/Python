# Description: Determine total bill for lawn care services. if you find this
# goes over multiple lines, Just add another comment.
# Author: Maurice & SD 14
# Dates: Jan 9, 2025 -
 
'''
Description: Determine total bill for lawn care services. if you find this
goes over multiple lines, Just add another comment.
Author: Maurice & SD 14
Dates: Jan 9, 2025 -
'''
# How do we add constants to the IPO Chart.
# Add comments to the top if you want.
# Between the comments and the input - set up constants.
 
# Assign 35.00 to the LABOR_RATE
# Assign .15 to the HST_RATE
 
 
# Define program constants.
BORDER_SIZE_RATE = .04 # 4% of the total lawn is border.
BORDER_COST_RATE = .35 # Border is charges at 35 cents per sq foot.
 
LAWN_SIZE_RATE = .96 # 96% of the total is the lawn area.
LAWN_COST_RATE = .07 # Lawn is charged at 7 cents per sq foot.
 
FERT_COST_RATE = .05 # Fert is charged at 5 cents per sq foot.
 
HST_RATE = .15 # Current rate to calulate the HST.
ENV_RATE = .03 # Environomental tax is calculated at 3%.
 
 
# Gather user input.
CustName = input("Enter the customer name: ")
StAdd = input("Enter the street address: ")
City = input("Enter the customer city: ")
Phone = input("Enter the customer phone number: ") # Not used in calcs - keep t s string.
 
TotSqFt = input("Enter the total square feet of the property: ")
TotSqFt = int(TotSqFt)
 
 
# Perform program calculations.
BorderSize = TotSqFt * BORDER_SIZE_RATE
BorderCost = BorderSize * BORDER_COST_RATE
 
LawnSize = TotSqFt * LAWN_SIZE_RATE
LawnCost = LawnSize * LAWN_COST_RATE
 
FertCost = TotSqFt * FERT_COST_RATE
TotalCharges = BorderCost + LawnCost + FertCost
 
HST = TotalCharges * HST_RATE
EnvTax = TotalCharges * ENV_RATE
InvTotal = TotalCharges + HST + EnvTax
 
 
# Display user results.
print()
print("Customer name:                   ", CustName)
print("Customer strret address:         ", StAdd)
print("Customer city:                   ", City)
print("Customer phone number:           ", Phone)
 
print()
print("Total sq footage for property:   ", TotSqFt)
 
print()
print("Total border area:               ", BorderSize)
print("Border cost:                     ", BorderCost)
 
print()
print("Total lawn area:                 ", LawnSize)
print("Lawn Cost:                       ", LawnCost)
 
print()
print("Fertilizer cost:                 ", FertCost)
 
print()
print("Total service charges:           ", TotalCharges)
print("HST (Sales Tax):                 ", HST)
print("Environmental tax:               ", EnvTax)
 
print()
print("Invoice total:                   ", InvTotal)