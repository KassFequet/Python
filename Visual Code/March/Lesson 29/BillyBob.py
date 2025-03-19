# Description: Billy Bob Rentals - HW
# Author: Kass
# Date(s):March 18/25


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
INV_NUM = 1358


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    print()
    CustName = input("Enter the customers name: ")
    CustPhone = input("Enter the customers phone number (XXX-XXX-XXXX): ")
    BikeCode = input("Enter the code for the bike rented (T OR M): ")
    BikeNum = input("Enter the number of bikes rented (1-3): ")
    CreditNum =  input("Enter the credit card number (XXXX-XXXX-XXXX-XXXX): ")
    CreditExp = input("Enter the credit card expiry date (YYYY-MM)")


    #Perform required calculations.



    # Display results



    # Write the values to a data file for storage.
    f = open("BikeRental.dat", "a")
    
    f.write(f"{CustName}, ")
    f.write(f"{CustPhone}, ")
    f.write(f"{BikeCode}, ")
    f.write(f"{BikeNum}, ")
    f.write(f"{CreditNum}, ")
    f.write(f"{CreditExp}, ")

    f.close()




    Continue = input("Do you want to process another bike rental (Y/N): ").upper()
    if Continue == "N":
        break


# Any housekeeping duties at the end of the program.
