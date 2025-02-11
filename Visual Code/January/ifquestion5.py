# Description: Template If Question 5
# Author: Kassaundra Fequet
# Date(s): January 22/24
 
 
# Define required libraries.
 
 
 
# Define program constants.

 
# Define program functions.
 
 
 
# Main program starts here.
 
   
# Gather user inputs.
TransType = input("Enter the type of transaction (D,W): ").upper()
BankBalance = input("Enter the current bank balance: ")
BankBalance = float(BankBalance)
TransAmount = input("Enter the transaction amount: ")
TransAmount = float(TransAmount)
 
# Perform required calculations.
if TransType == "D":
    NewBalance = BankBalance + TransAmount
    TransName = "Deposit"
elif TransType == "W":
    if TransAmount > BankBalance: 
        NewBalance = BankBalance  # Balance remains unchanged
        TransName = "Withdrawal Denied: Insufficent Funds"
    else:
        NewBalance = BankBalance - TransAmount
        TransName = "Withdrawal"


# Display results
print()
print(f"Transaction Type:         {TransName}")
print(f"Original Balance:         ${BankBalance:,.2f}")
print(f"Transaction Amount:       ${TransAmount:,.2f}")
print(f"New Balance:              ${NewBalance:,.2f}")


# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.