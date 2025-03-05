# Define required libraries.
from datetime import datetime, timedelta


# Define program constants.
BASE_SAL = 350.00
SALES_QUOTA = 5000.00


# Long or complex calculations of a single value can be placed in a function.
# The resulting value calculated in the function is returned to the program.

# If any variables are required, they must be passed in as parameters.
# In this example, i will need the Number Grade.

def LetterGrade(NumGrade):
    #Convert a number grade to a letter grade.
    
    if NumGrade >=80 and NumGrade <= 100:
        LetterGrade = "A"
    elif NumGrade >= 70 and NumGrade <= 79:
        LetterGrade = "B"
    elif NumGrade >= 60 and NumGrade <= 69:
        LetterGrade = "C"
    elif NumGrade >= 50 and NumGrade <= 59:
        LetterGrade = "D"
    else:
        LetterGrade = "F"
    
    return LetterGrade


def WeekGrossPay(NumHours, PayRate):
    # Calculate the weekly gross pay based on 1.5 times overtime after 40 hours.
    
    if NumHours <= 40:
        GrossPay = NumHours * PayRate
    else:
        RegPay = 40 * PayRate
        OTPay = (NumHours -40) * (PayRate * 1.5)
        GrossPay = RegPay + OTPay
        
    return GrossPay

def EmpBonus(TotalSales):
    #Calculate and return the bonus for an employee
    
    Bonus = TotalSales * .01
    if TotalSales < 5000.00:
        Bonus = 0
    elif TotalSales > 100000.00:
        Bonus += 500.00
        
    return Bonus
    
def TrainHeart(Age, RestHeartRate):
    #Calculate the ideal training heart rate for a person.

    TrainHeartRate = (((220 - Age) - RestHeartRate) * .60) + RestHeartRate

    return TrainHeartRate

def Sum(Number):
    # Calculate the sum of all numbers up to and including the given value.
    TotalSum = sum(range(1, Number + 1))
    return TotalSum



def PaymentDate(purchase_date):
    # Convert the purchase_date string to a datetime object
    purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
    
    # Determine the first day of the next month
    if purchase_date.day >= 25:
        # Add an extra month if the day is 25 or greater
        if purchase_date.month == 12:
            payment_date = datetime(purchase_date.year + 1, 2, 1)
        else:
            payment_date = datetime(purchase_date.year, purchase_date.month + 2, 1)
    else:
        if purchase_date.month == 12:
            payment_date = datetime(purchase_date.year + 1, 1, 1)
        else:
            payment_date = datetime(purchase_date.year, purchase_date.month + 1, 1)
    
    return payment_date.strftime("%Y-%m-%d")

def IsEven(number):
    """
    Check if a given number is even.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is even, False if the number is odd.
    """
    return number % 2 == 0

def GetPayDate(PurchaseDate):
    #Calculate the first payment date as the first day of the next month.
    
    PurYear = PurchaseDate.year
    PurMonth = PurchaseDate.month
    PurDay = PurchaseDate.day
    
    PayYear = PurYear
    PayMonth = PurMonth + 1
    #If the day of the month is the 25th or greater, add 1 to the month.
    if PurDay >= 25:
        PayMonth += 1
    #The month must be between 1 and 12. If it gets to 13, make the pay month 1 and add 1 to the year.
    if PayMonth > 12:
        PayMonth = PayMonth - 12
        PayYear += 1
        
    PayDay = 1
    
    PayDate = datetime.datetime(PayYear, PayMonth, PayDay)
    
    return PayDate
    
def GrossDraw(TotalSales):
    #Calculate a gross pay based on a draw against commission.
    
    if TotalSales < SALES_QUOTA:
        Under = SALES_QUOTA - TotalSales
        DedAmt = Under * .10
        GrossPay = BASE_SAL - DedAmt
    else:
        Comm = TotalSales * .04
        GrossPay = BASE_SAL + Comm
        if TotalSales > 20000.00:
            GrossPay += 500.00
        elif TotalSales >10000.00:
            GrossPay += 200.00
            
    return GrossPay
            
    
    
