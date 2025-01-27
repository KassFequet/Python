# Description: The Gym
# Author: Mo and Class
# Date(s): January 22/2025
 
 
# Define required libraries.
 
 
 
# Define program constants.
MEM_COST = 125.00
ADD_MEM_COST = 75.00

TOWEL_COST = 7.00
EXEC_COST = 18.00

INIT_MEM_FEE = 49.99

HST_RATE = .15
CAN_RATE = .60

 
# Define program functions.
 
 
 
# Main program starts here.
 

   
# Gather user inputs.
MemNum = input("Enter the membership number (00000):  ")
NumFamMem = input("Enter the number of family members: ")
NumFamMem = int(NumFamMem)
TowelServ = input("Do you want extra towel service (Y/N): ").upper()
ExecTreat = input("Do you want the executive service(Y/N): ")
CurDay = input(" Enter the current day of the month (1-31):")
CurDay = int(CurDay)
CurMon = input("Enter the current month (1-12): ")
CurMon = int(CurMon)
CurYear = input("Enter the current year (0000): ")
CurYear = int(CurYear)
 
# Perform required calculations.
MemCost = MEM_COST + (NumFamMem -1) *  ADD_MEM_COST

if TowelServ == "Y":
    TowelCost = TOWEL_COST
else:
    TowelCost = 0

if ExecTreat =="Y":
    ExecCost = EXEC_COST
else:
    ExecCost = 0
TotalExtraCost = TowelCost + ExecCost

MonFees = MemCost + TotalExtraCost
HSTMonFees = MonFees * HST_RATE
TotalMonPay = MonFees + HSTMonFees


if CurMon == 1:
    TotalDays = 31
elif CurMon == 2:
    TotalDays = 28
    if CurYear % 4 == 0 : #Means easily diivisible by 4 bc thats a leap year.
        TotalDays = 29
    if CurYear % 100 == 0: #not a leap year
        TotalDays = 28
    if CurYear % 400 ==0: #leap year
        TotalDays = 29
elif CurMon == 3:
    TotalDays = 31
elif CurMon == 4:
    TotalDays = 30
elif CurMon == 5:
    TotalDays = 31
elif CurMon == 6:
    TotalDays = 30
elif CurMon == 7:
    TotalDays = 31
elif CurMon == 8:
    TotalDays = 31
elif CurMon == 9:
    TotalDays = 30
elif CurMon == 10:
    TotalDays = 31
elif CurMon == 11:
    TotalDays = 30
elif CurMon == 12:
    TotalDays = 31

DaysLeft = TotalDays - CurDay 
ProRatedPer = DaysLeft / TotalDays 
ProRatedMemCost = MonFees * ProRatedPer

RegFee = INIT_MEM_FEE + ProRatedMemCost
HSTRegFee = RegFee * HST_RATE
TotalDueAtSigning = RegFee + HSTRegFee

CanFee = (MemCost * 3) *CAN_RATE



# Display results



# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.