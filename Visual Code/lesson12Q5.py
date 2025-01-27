# Description: Lesson 12 Question 5 - Museum Price Challenge
# Author: Kassaundra Fequet
# Date(s): Jan 24/25
 
 
# Define required libraries.
 
 
 
# Define program constants.
ADMIN_PRICE = 22.50
 

# Define program functions.
 
 
 
# Main program starts here.
 

   
# Gather user inputs.
Weekday=input("Enter the day of the week: ").upper()
Age=input("Enter your age: ")
Age = int(Age)
 
 
# Perform required calculations.
if Weekday =="MONDAY":
    Display = "We are closed on Mondays"
elif Weekday =="TUESDAY":
    Price = ADMIN_PRICE * .5
elif Weekday =="WEDNESDAY":
    if Age >=13 and Age <=20:
        Price = ADMIN_PRICE * .75
    if Age <=13 and Age >=20:
        Price = ADMIN_PRICE
elif Weekday =="THURSDAY":
    Price = ADMIN_PRICE * .5




# Display results
print(Price)


# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.