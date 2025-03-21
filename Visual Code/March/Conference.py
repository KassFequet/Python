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

    ClientName = input("Enter the clients name (End to finish): )").title()
    if ClientName == "End":
        break
    ConfTitle = input("Enter the conference title: ").title()
    
    StartDate = input("Enter the start date of the conference (YYYY-MM-DD):")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    
    NumDays = input("Enter the total number of days: ")
    NumDays = int(NumDays)
    
    MaxAtt = input("Enter the maximum number of people attending: ")
    MaxAtt = int(MaxAtt)
    
    NumBreak = input("Enter the number of breakfasts: ")
    NumBreak = int(NumBreak)
    NumLunch = input("Enter the number of lunches: ")
    NumLunch = int(NumLunch)
    NumSupper = input("Enter the number of suppers: ")
    NumSupper = int(NumSupper)
    NumCoffee = input("Enter the number of coffee breaks: ")
    NumCoffee = int(NumCoffee)


    #Perform required calculations.
    
    if MaxAtt <= 30:
        TotRoomCost =NumDays * SMALL_COST
    elif MaxAtt <= 100:
        TotRoomCost = NumDays * MED_COST
    else:
        TotRoomCost = NumDays * LARGE_COST
        
    BreakCost = NumBreak * MaxAtt * BREAK_COST
    LunchCost = NumLunch * MaxAtt * LUNCH_COST
    SupperCost = NumSupper * MaxAtt * SUPPER_COST
    CoffeeCost = NumCoffee * MaxAtt * COFFEE_COST
    TotFoodCost = BreakCost + LunchCost + SupperCost + CoffeeCost
    
    EstConfCost = TotRoomCost + TotFoodCost
    
    HST = EstConfCost * HST_RATE
    ConfTotal = EstConfCost + HST
    
    CostPerAtt = ConfTotal / MaxAtt
    
    
    
    # Display results
    print(f"Conference total cost:       {FV.FDollar2(ConfTotal):>10s}")
    print()
    print(f"Cost per Attendee:           {FV.FDollar2(CostPerAtt):>10s}")
    


    # Write the values to a data file for storage.
    f = open("Conference.dat", "a")
    
    f.write(f"{str(NEXT_CONF_NUM)}, ") # str() or FV.Number0() - just store the number, no $ or commas
    f.write(f"{ClientName}, ")
    f.write(f"{ConfTitle}, ")
    f.write(f"{FV.FDateS(StartDate)}, ")
    f.write(f"{str(NumDays)}, ")
    f.write(f"{str(MaxAtt)}, ")
    f.write(f"{str(NumBreak)}, ")
    f.write(f"{str(NumLunch)}, ")
    f.write(f"{str(NumSupper)}, ")
    f.write(f"{str(NumCoffee)}, ")
    f.write(f"{FV.FNumber2(ConfTotal)}, ")
    f.write(f"{FV.FNumber2(CostPerAtt)}\n")
    
    f.close()
    
    print()
    print("    Conference data has been successfully saved.")
    print()
    
    #Update any values for the next conference booking.
    NEXT_CONF_NUM += 1
    
    #Update the defauls file here
    f = open("CCDef.dat", "a")
    
    f.write(f"{FV.FNumber0(NEXT_CONF_NUM)}\n")
    f.write(f"{FV.FNumber2(HST_RATE)}\n")
    f.write(f"{FV.FNumber2(SMALL_COST)}\n")
    f.write(f"{FV.FNumber2(MED_COST)}\n")
    f.write(f"{FV.FNumber2(LARGE_COST)}\n")
    f.write(f"{FV.FNumber2(BREAK_COST)}\n")
    f.write(f"{FV.FNumber2(LUNCH_COST)}\n")
    f.write(f"{FV.FNumber2(SUPPER_COST)}\n")
    f.write(f"{FV.FNumber2(COFFEE_COST)}\n")
    
    f.close()


# Any housekeeping duties at the end of the program.
# Update the defaults file here.