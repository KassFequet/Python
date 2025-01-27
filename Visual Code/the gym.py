 # Desc: Determine membership costs for The Gym.
# Author: Maurice & SD 14
# Date: Jan 13. 2025
 
# Define program constants.
MEM_RATE = 125.00
ADD_MEM_RATE = 75.00
TOWEL_RATE = 6.00
MAIN_RATE = .01 # 1% of the membership fee
HST_RATE = .15
CAN_RATE = .60 # 60% of 3 months of the membership cost.
 
# Gather user input.
print()
MemNum = input("Enter the membership number (#####): ")
MemName = input("Enter the membr name: ")
StAdd = input("Enter the street address: ")
Phone = input("Enter the phone number (###-###-####): ")
 
print()
NumMembers = input("Enter the number of family members: ")
NumMembers = int(NumMembers)
 
# Calculate program results.
MemCost = MEM_RATE + (NumMembers - 1) * ADD_MEM_RATE
TowelCost = TOWEL_RATE
MainCost = MemCost * MAIN_RATE
TotMemFee = MemCost + TowelCost + MainCost
 
HST = TotMemFee * HST_RATE
TotMemCost = TotMemFee + HST
 
CanCost = (MemCost * 3) * CAN_RATE
 
# Display program results.
# The f-string allows us to create a single string for a line of output.
# Headings and punctuation appear as needed, variables are defined in {}.
 
print()
print(f"Membership number:            {MemNum:<5s}") # 5 digit number
print(f"Member name:                  {MemName:<25s}")
print(f"Street address:               {StAdd:<25s}")
print(f"Phone number:                 {Phone:<12s}")
# Phone can be 8 characters: 123-1234, 10 char: 1231231234
# 12 char: 123-123-1234, 14 char: (123) 123-1234
 
print(f"Number of family members:     {NumMembers:>2d}")
 
MemCostDsp = "${:,.2f}".format(MemCost)
print(f"Membership cost:              {MemCostDsp:>7s}") # $123.45
HSTDsp = "${:,.2f}".format(HST)
print(f"HST:                          {HSTDsp:>7s}")     #  $17.36
 

 
 