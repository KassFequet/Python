# Description: Claims Processing Program - claims are stored in a file called Claims.dat
# Author:Mo and Class
# Date(s): March 17/25


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
CLAIM_NUM = 34
HST_RATE = .15

CUR_DATE = datetime.datetime.now()


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    print()
    EmpNum = input("Enter the employee number (END to finish): ").upper()
    if EmpNum == "END":
        break
    EmpName = input("Enter the employee name: ")
    Location = input("Enter the trip location: ")
    
    StartDate = input("Enter the start date (YYY-MM-DD): ")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    EndDate = input("Enter the end date (YYY-MM-DD): ")
    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    
    OwnRent = input("Did you rent a car or use your own vehicle (R/O): ").upper()
    TotKilos = 0
    if OwnRent == "O":
        TotKilos = input("Enter the total number of kilometers travelled: ")
        TotKilos = float(TotKilos)

    #Perform required calculations.
    NumDays = (EndDate - StartDate).days
    if NumDays <= 3:
        PerDiemAmt = NumDays * 85.00
    else:
        PerDiemAmt = NumDays * 100.00
        
    if OwnRent == "O":
        MilAmt = TotKilos * .10
    else: MilAmt = NumDays * 56.00
    
    ClaimAmt = PerDiemAmt + MilAmt
    HST = ClaimAmt * HST_RATE
    TotalClaim = ClaimAmt + HST


    # Display results
    print()
    print(NumDays)
    print(TotalClaim)


    # Write the values to a data file for storage.
    f = open("Claims.dat", "a") #The "a" is the mode = append adds to the end of the file.
    #Also use "w" for write - that will overwrite the file with the new data.
    
    f.write(f"{CLAIM_NUM}, ") #All values written to a file must be a string
    f.write(f"{FV.FDateS(CUR_DATE)}, ")   # This is the current system date – you may want to format it so that the time does not appear.
    
    f.write(f"{EmpNum}, ")
    f.write(f"{EmpName}, ")
    f.write(f"{Location}, ")
    f.write(f"{ FV.FDateS(StartDate)}, ")
    f.write(f"{ FV.FDateS(EndDate)}, ")
    f.write(f"{str(NumDays)}, ")
    f.write(f"{str(TotKilos)}, ")
    #ClaimTotal= round(ClaimTotal, 2)   # May want to round floats to remove excess decimals.
    #f.write(f"{str(ClaimTotal)}\n")
    f.write(f"{FV.FNumber2(TotalClaim)}\n") #The number format is just numbers, no
    
    f.close()

    #Every value here must be a string so either str it or format it.
    
    #Display a message for the user to let them know the data is saved.
    print()
    print("Claim information has been successfully saved.")
    print()
    
    #Update any values for the next claim processing.
    CLAIM_NUM += 1
    
# Any housekeeping duties at the end of the program.