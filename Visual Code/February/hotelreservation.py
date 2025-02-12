# Description:Hotel Reservation system
# Author:Mo and Class
# Date(s):Feb 12/25


# Define required libraries.
import datetime


# Define program constants.
NIGHT_RATE_LOW = 85.00
NIGHT_RATE_HIGH = 105.00

CUR_DATE = datetime.datetime.now()


# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    print(f"The Hotel Reservation System")
    print()
    
    while True:
        try:
            ArrDate = input("Enter the arrival date (YYYY-MM-DD):     ")
            ArrDate = datetime.datetime.strptime(ArrDate, "%Y-%m-%d")
        except:
            print("    Error - date is invalid.  Use YYYY-MM-DD format.")
        else:
            # Validate to ensure it is not a future date.
            if ArrDate > CUR_DATE:
                print("    Error - cannot enter an arrival date in the future.")
            else:
                break

    while True:
        try:
            DepDate = input("Enter the departure date (YYYY-MM-DD): ")
            DepDate = datetime.datetime.strptime(DepDate, "%Y-%m-%d")
        except:
            print("    Error - date is invalid.  Use YYYY-MM-DD format.")
        else:
            # Validate that the dep date is after the arv date.
            if DepDate < ArrDate:
                print("    Error - cannot enter a departure date prior to the arrival date.")
            else:
                break
            

    # Perform required calculations.
    ArrMonth = ArrDate.month
    #could also do Msg ="" here
    if ArrMonth == 7 or ArrMonth == 8:
        NightlyRate = NIGHT_RATE_HIGH
        Msg = "(High Season Rate Applied)"
    else:
        NightlyRate = NIGHT_RATE_LOW
        Msg = ""
        
    # If an arrival is June 29th and the departure is July 2nd - you now have 2 days in the low and 2 days in the high.
    
    NumNights = (DepDate - ArrDate).days
    
    TotalPrice = NightlyRate * NumNights
    


    # Display results
    print()
    ArrDateDsp = datetime.datetime.strftime(ArrDate, "%B %d, %Y")
    print(f"Arrival date:     {ArrDateDsp:<20s}")
    
    DepDateDsp = datetime.datetime.strftime(DepDate, "%B %d, %Y")
    print(f"Departure date:   {DepDateDsp:<20s}")
    
    NightlyRateDsp = "${:,.2f}".format(NightlyRate)
    print(f"Nightly rate:     {NightlyRateDsp:>6s} {Msg:<26s}")
    
    print(f"Total nights:     {NumNights:>1d}")
    
    TotalPriceDsp = "${:,.2f}".format(TotalPrice)
    print(f"Total price:      {TotalPriceDsp:>6s}")
    print()


    # Write the values to a data file for storage.

    while True:
        Continue = input("Continue (Y/N): ").upper()
        
        if Continue != "Y" and Continue != "N":
            print("    Error - option to continue should be Y or N only")
        else:
            break
        
    if Continue == "N":
        break

# Any housekeeping duties at the end of the program.
print()
print(f"Thank you for using the Hotel Reservation Program. Bye Bye.")