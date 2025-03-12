# Description: Real Estate Help - Lesson 25/25 - Question 3 - HW
# Author: Kass
# Date(s): Mar 11/25


# Define required libraries.
import datetime


# Define program constants.



# Define program functions.



# Main program starts here.
def GetStatus():
    ValidStatus = ["Open", "Offer Pending", "Sold"]
    while True:
        Status = input("Enter the status (Open, Offer Pending, Sold): ").title()
        if Status in ValidStatus:
            return Status
        else:
            print()
            print("Invalid Status - Enter either Open, Offer Pending or Sold.")
            print()
            
def GetDatePrice():
    DatePrice = []
    while True:
        Date = input("Enter the date (YYY-MM-DD) or done to finish program: )").lower()
        if Date == "done":
            break
        try:
            Date = datetime.datetime.strptime(Date, "%Y-%m-%d").date()
        except ValueError:
            print()
            print("Invalid Date Format - Enter date as YYYY-MM-DD")
            print()
            
        Price = input("Enter the listing price: ")
        Price = float(Price)
        
        DatePrice.append(Date, Price)
    return DatePrice

def MainList():
    Listings = []
    
    while True:
        


# Gather user inputs.



#Perform required calculations.



# Display results



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.