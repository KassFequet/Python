# Description: Lesson 21 - Functions
# Author: Mo and class
# Date(s): March 3/25


# Define required libraries.
from datetime import datetime, timedelta


# Define program constants.



# Define program functions.
def PrintMsg():
    # Comment to explain the use of the function.
    
    print()
    print("*****************************************")
    print("Thank You For Playing With Mo's Menu")
    print("*****************************************")
    print()
    
def CelToFahr():
    #Convert a celsius temperature to Fahrenheit and display the result
    print()
    CelTemp = input("Enter the temperature in Celsius:")
    CelTemp = float(CelTemp)
    
    FahrTemp = 9 / 5 * CelTemp + 32
    
    FahrTempDsp = "{:.1f}".format(FahrTemp)
    print()
    print(f"The fahrenheit temperature is {FahrTempDsp}.")
    print()

def TrainingHR():
    #Determine and display the ideal training heart rate for a person.
    print("This is Option 2 from the menu")
    pass # If you want to pass the function - code will be added later.

def DaysToChristmas():
    #Determine the number of days from the current date to the next Christmas day.
    print("This is Option 3 from the menu")
    pass

def InvoiceAge():
    # Determine the age of an invoice.
    print("This is Option 4 from the menu")
    pass

def GuessingGame():
    # Play my guessing game. It is so much fun.
    print("This is Option 5 from the menu")
    pass

def PassStrength(): #Found from Mo
    #Check the strength of an entered password.
    
    allowed_num = set("1234567890")
    allowed_upper_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_lower_char = set("abcdefghijklmnopqrstuvwxyz")

    while True:
        Password = input("Enter a strong password: ")

        UpperCtr = 0
        LowerCtr = 0
        NumCtr = 0
        SpecCtr = 0

        for Char in Password: # Loop through each character in the password from index 0 to the end.
            if set(Char).issubset(allowed_num) == True:
                NumCtr += 1
            elif set(Char).issubset(allowed_upper_char) == True:
                UpperCtr += 1
            elif set(Char).issubset(allowed_lower_char) == True:
                LowerCtr += 1
            else:
                SpecCtr += 1

        if len(Password) < 7:
            print("   Error - Password must be at least 7 characters.")
        elif UpperCtr == 0:
            print("   Error - Password must contain at least one uppercase character.")
        elif LowerCtr == 0:
            print("   Error - Password must contain at least one lowercase character.")
        elif NumCtr == 0:
            print("   Error - Password must contain at least one numeric character.")
        elif SpecCtr == 0:
            print("   Error - Password must contain at least one special character.")
        else:
            break
    pass

def EmpBenefits(): #Copilot
    # Determine when an employee can get enrolled in company benefits.
    print("This is Option 7 from the menu")
    
    start_date_str = input("Enter the employee's start date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    # Calculate benefit dates
    medical_benefits_date = start_date + timedelta(days=90)
    rrsp_benefits_date = start_date + timedelta(days=180)
    
    # Calculate retirement date
    retirement_date = start_date.replace(year=start_date.year + (65 - start_date.year))
    days_to_retirement = (retirement_date - datetime.now()).days
    
    # Display the results
    print()
    print(f"Employee's start date: {start_date.date()}")
    print(f"Medical benefits start date: {medical_benefits_date.date()}")
    print(f"RRSP benefits start date: {rrsp_benefits_date.date()}")
    print(f"Days to retirement: {days_to_retirement}")
    print()
    
    pass

def SumNum(): #Copilot
    # Determine the sum of numbers up to an entered value.
    print("This is Option 8 from the menu")
    n = int(input("Enter a number: "))
    total_sum = sum(range(1, n + 1))
    print(f"The sum of all numbers from 1 to {n} is {total_sum}.")
    pass

def ChangeReturn():
    # To determine each denomination required for change on a purchase.
    print()
    cost = float(input("Enter the cost of the item: "))
    amount_given = float(input("Enter the amount of money given: "))
    
    # Calculate the change in cents
    change = int((amount_given - cost) * 100)
    
    if change < 0:
        print("Error: The amount given is less than the cost of the item.")
        return
    
    # Calculate the number of quarters, dimes, and nickels
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    change %= 5
    pennies = change  # Remaining change in pennies
    
    # Display the results
    print()
    print(f"Change to be returned: {amount_given - cost:.2f}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")
    print()
    
    pass


# Main program starts here.
while True:


    # Gather user inputs.
    # Call a function by referencing the name.
    print()
    print("Mo's Quick Problems - Main Menu")
    print()
    
    print("1. Convert Celsius to Fahrenheit")
    print("2. Determine Training Heart Rate")
    print("3. How Many Days to Christmas")
    print("4. How old is the invoice?")
    print("5. Play My Guessing Game")
    print("6. Check password strength")
    print("7. When can an employee get benefits")
    print("8. Get the sum of all numbers")
    print("9. Change return calculator.")
    print("10. Quit")
    print()
    
    Choice = input("Enter choice: (1-10):  ")
    Choice = int(Choice) #Can do an int or leave as a string. Doesn't matter.
    #Would also need to validate.



    #Perform required calculations.
    #Each option from the menu is set up in a function. That makes this area of the program much cleaner and better organized.
    
    if Choice == 1:
        CelToFahr() #Could also set up a seperate program and import it here.
    elif Choice == 2:
        TrainingHR()
    elif Choice == 3:
        DaysToChristmas()
    elif Choice == 4:
        InvoiceAge()
    elif Choice == 5:
        GuessingGame()
    elif Choice == 6:
        PassStrength()
    elif Choice == 7:
        EmpBenefits()
    elif Choice == 8:
        SumNum()
    elif Choice == 9:
        ChangeReturn()
    else:
        break


    # Display results
    



    # Write the values to a data file for storage.


# Any housekeeping duties at the end of the program.
PrintMsg()