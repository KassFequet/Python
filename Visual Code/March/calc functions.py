# Description: Lesson 22/23
# Author: Mo and Class
# Date(s): March 4/25


# Define required libraries.
from datetime import datetime, timedelta
import FunLib as FL


# Define program constants.
BASE_SAL = 350.00
SALES_QUOTA = 5000.00


# Define program functions.

#Imported from FunLib file.


# Main program starts here.
while True:


    # Gather user inputs.



    #Perform required calculations.
    
    '''
    # Test the LetterGrade() function.
    print(LetterGrade(84))

    #OR
    Grade = input("Enter the student grade (0 - 100): ")
    Grade = int(Grade)
    
    # Functions that perform calcs in this way are always on the right side of the equal sign.
    Letter = LetterGrade(Grade)
    print(Letter)


    #TestWeekGrossPay() Function/
    Hours = 35
    Rate = 16.00
    
    GrossPay = WeekGrossPay(Hours, Rate)
    print(GrossPay)
    
    
    #Test the EmpBonus() function.
    Sales = 50000.00
    
    Bonus = EmpBonus(Sales)
    print(Bonus)
    
    '''
    # Display results
    Age = 25
    RestHeartRate = 80


    TrainingHeart = TrainHeart(Age, RestHeartRate)
    print(TrainingHeart)
    
    purchase_date = "2022-02-14"
    print(PaymentDate(purchase_date))  # Output: 2022-03-01

    purchase_date = "2022-02-26"
    print(PaymentDate(purchase_date))  # Output: 2022-04-01
    
    # Example usage
    number = 42
    result = IsEven(number)
    print(f"Is {number} even? {result}")

    number = 33
    result = IsEven(number)
    print(f"Is {number} even? {result}")
    
    PurDate = datetime.datetime.now()
    
    FirstPayDate = GetPayDate(PurDate)
    
    print(FirstPayDate)


    #Test the GrossDraw() function
    TotSales = 6000.00
    
    
    
    GrossPay =FL.GrossDraw(TotSales)
    print(GrossPay)
    
    # Write the values to a data file for storage.
    
    Cont = input("Press Enter to continue.")


# Any housekeeping duties at the end of the program.