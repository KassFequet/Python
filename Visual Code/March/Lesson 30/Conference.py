# Description: Generate and store conference information
# Author: Mo and Class
# Date(s): Mar 20/25


# Define required libraries.
import datetime
import FormatValues as FV



# Define program constants.
f = open('CCDef.dat', 'r')
NEXT_CONF_NUM = int(f.readline())
HST_RATE = float(f.readline())
SMALL_COST = float(f.readline())
MED_COST = float(f.readline())
LARGE_COST = float(f.readline())
BREAK_COST = float(f.readline())
LUNCH_COST = float(f.readline())
SUPPER_COST = float(f.readline())
COFFEE_COST = float(f.readline())

f.close()


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    print(NEXT_CONF_NUM)
    print(MED_COST)
    print(SUPPER_COST)


    #Perform required calculations.
    ClientName = input("Enter the clients name (End to finish): )").title()
    ConfTitle = input("Enter the conference title: ").title()
    NumDays = input("Enter the total number of days: ")
    NumDays = int(NumDays)
    
    MaxAtt = input("Enter the maximum number of people attending: ")
    MaxAtt = int(MaxAtt)


    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.