# Description: Template
# Author:
# Date(s):


# Define required libraries.



# Define program constants.



# Define program functions.

# Description: Template
# Author:
# Date(s):

# Define required libraries.


'''
# Define program constants.
DISCOUNT_RATE = 0.02
DISCOUNT_DAYS = 10
DUE_DAYS = 30

# Define program functions.

# Main program starts here.

# Gather user inputs.
invoice_date_str = input("Enter the date of the sales invoice (YYYY-MM-DD): ")
invoice_amount = float(input("Enter the amount of the invoice: "))

# Convert invoice date string to datetime object
invoice_date = datetime.strptime(invoice_date_str, "%Y-%m-%d")

# Perform required calculations.
discount_date = invoice_date + timedelta(days=DISCOUNT_DAYS)
due_date = invoice_date + timedelta(days=DUE_DAYS)
discount_amount = invoice_amount * (1 - DISCOUNT_RATE)
current_date = datetime.now()
invoice_age = (current_date - invoice_date).days

# Display results
print("\nInvoice Details")
print("----------------")
print(f"Original Amount:          ${invoice_amount:,.2f}")
print(f"Discount Date:            {discount_date.strftime('%Y-%m-%d')}")
print(f"Amount Due with Discount: ${discount_amount:,.2f}")
print(f"Due Date:                 {due_date.strftime('%Y-%m-%d')}")
print(f"Current Age of Invoice:   {invoice_age} days")
'''
import datetime

#CONSTANT
NightRate = 85.00
HighNightRate = 105.00

arvdate = input("Enter the arrival date: ")
depdate = input("Enter the departure date: ")


arvdatetime = datetime.datetime.strptime(arvdate, "%Y-%m-%d")
depdatetime = datetime.datetime.strptime(depdate, "%Y-%m-%d")

arvmonth = arvdatetime.month
depmonth = depdatetime.month

if arvmonth in [7, 8]:  # High season months: July, August
    rate = HighNightRate
else:
    rate = NightRate
    
num_nights = (depdatetime - arvdatetime).days

total_cost = num_nights * rate

print(f"Arrival date:     {arvdatetime.strftime('%B %d, %Y')}")
print(f"Departure date:   {depdatetime.strftime('%B %d, %Y')}")
print(f"Number of nights: {num_nights}")
print(f"Rate per night:   ${rate:,.2f}")
print(f"Total cost:       ${total_cost:,.2f}")



# Write the values to a data file for storage.
# ...existing code...

# Main program starts here.



# Gather user inputs.



# Perform required calculations.



# Display results



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.