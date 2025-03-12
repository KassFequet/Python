# Description: ABC Payroll with functions
# Author: Mo and Class
# Date(s): Mar 6/25


# Define required libraries.
import FormatValues as FV
import ABCFunctions as AF
import datetime


# Define program constants.
INC_TAX_RATE = .20
EI_RATE = .028
CPP_RATE = .049

BEN_SELF_RATE = 52.00
BEN_FAM_RATE = 135.00
BEN_NO_RATE = 18.00

BASE_SAL = 500.00

CUR_DATE = datetime.datetime.now()


# Define program functions.
#   See imported library ABCFunctions.


# Main program starts here.
while True:


    # Gather user inputs.
    FirstName = "John"
    LastName = "Smith"
    SIN = "123123123"
    MedBen = "F".upper()
    WeeklySales = 7450.00
    ExtraIncTax = 20.00
    RRSPCont = "Y".upper()
    RRSPAmt = 0
    if RRSPCont == "Y":
        RRSPAmt = 75.00
        
    


    #Perform required calculations.
    Comm = AF.GetComm(WeeklySales)
    
    #Include any constants from the program as needed in a function by adding it as a parameter
    GrossPay = AF.FindGrossPay(WeeklySales, Comm, BASE_SAL)
    
    IncTax = (GrossPay * INC_TAX_RATE)+ ExtraIncTax
    EI = GrossPay * EI_RATE
    CPP = GrossPay * CPP_RATE
    
    if MedBen == "S":
        MedAmt = BEN_SELF_RATE
    elif MedBen == "F":
        MedAmt = BEN_FAM_RATE
    else:
        MedAmt = BEN_NO_RATE
        
    TotExtraDeds = MedAmt + RRSPAmt
    
    NetPay = GrossPay - (IncTax + EI + CPP + TotExtraDeds)


    

    # Display results
    
    #USe the function in the FarmatValues library to format the values.
    # OR CommDsp = FV.FDollar2(Comm) instead of formatting in the print section
    #print(f"Commission:                {CommDsp:>10s}")
    
    #print(f"Commission:                 {FV.FDollar2(Comm):>10s}")

    print()
    print(f"ABC Company - Payroll Calculations as of {FV.FDateM(CUR_DATE):>9s}")
    print()
    FullName = FirstName + " " + LastName
    print(f"Employee name: {FullName:>25s}         SIN: {SIN:>9s}")
    print()
    print(f"Commission:     {FV.FDollar2(Comm):>9s}   Income Tax:      {FV.FDollar2(IncTax):>9s}")
    print(f"Base Salary:     {FV.FDollar2(BASE_SAL):>9s} EI:      {FV.FDollar2(EI):>9s}")
    print(f"                  ---------                  ---------")
    
    

    # Write the values to a data file for storage.


    Continue = input("Do you want to process another employee (Y/N): ").upper() #would normally validate
    if Continue == "N":
        break
# Any housekeeping duties at the end of the program.