# Description: Template
# Author:
# Date(s):


# Define required libraries.
import random
import math
import datetime


# Define program constants.



# Define program functions.



# Main program starts here.
#Variables with values are referred to as objects. We are able to define methods on these objects to chnage behaviours.



DeptName = input("Enter the department name: ").title() #.capitalize does the first latter of it all in caps. .title does the first of each word in caps.

print(DeptName)

FullName = "john o'reilly-smith".title()
print(FullName)

#When you input a string, ask about case - .upper(), .capitalize() or .title()


CurDate = "2025-02-05"
CustFirst = "Alex".title()
CustLast = "Smith".title()
LocCode = "AJRD".upper()
TransCode = 14974
CustCtr = random.randint(1000, 9999) #This goes into the random library and will give us a random inteter between those numbers. theres also.random for random numbers.
#To generate a radom number, import the random library and use either random.random() for a number between 0-1 (can also multipy it by a number to get the range you want) or randint(100, 1000) - in this case you can specify a start and ending value for a range.
print(CustCtr)

#These grabbing sections are based on strings (concatennate), not numbers. SO they need to be strings. The str in front of transcode turns it into a string.
TrackNo = CustFirst[0] + CustLast[0] + "-" + LocCode[0:2] + "-" + str(TransCode)[3:6] + "-" + CurDate[0:4] + str(CustCtr)
print(f"{TrackNo:<17s}")


#Input and validate a phone number as 0000000000 and format to (000) 000-0000
while True:
    PhoneNum =input("Enter the phone number (0000000000): ")
    
    if PhoneNum == "":
        print("Error - cannot be blank")
    elif len(PhoneNum) != 10:
        print("Error - must be 10 characters only.")
    elif PhoneNum.isdigit() == False: #This checks the value tp see if its all digits.
        print("Error - must be all digits.")
    else:
        break

#At this point we have a value in the format 0000000000.
PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
print(PhoneNum)


#Do the other 2 as practice.
# Gather user inputs.



# Perform required calculations.



# Display results



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.