#Description: iafhai
#Author: Maurice and class
#Date(s): Jan 21,2025 - 
#IPO Outline Example

#Define required libraries



#Define program constants
RENTAL_RATE = 35.00
KILO_RATE = .10
FREE_KM_PER_DAY = 100

#Define program functions. 


#Main program starts here


#Gather user inputs.

#If a value can be defined as an integer, do that as it takes up half the storage as a float.
NumDays = input("Enter the number of days the car was rented: ")
NumDays = int(NumDays)
OdoRent = input("Enter the odometer reading when rented (99999): ")
OdoRent = int(OdoRent)
OdoReturn = input("Enter the odometer reading when returned: ")
OdoReturn = int(OdoReturn)

#Perfrom required calculations.

# ODometer can roll over when it reaches 100000. Check to see if it roelled over and do the calculations accordingly. 
if OdoReturn > OdoRent : #This is the most common case
    KMTrav = OdoReturn - OdoRent
else:
    KmTrav = (100000 - OdoRent) + OdoReturn

DailyCharge = NumDays * RENTAL_RATE

FreeMil = NumDays * FREE_KM_PER_DAY
if KMTrav <= FreeMil:
    ExtraKM = 0
else: 
    KMCharge = (KMTrav - FreeMil) * KILO_RATE

TotalCharge = DailyCharge + KMCharge
    

#Display results.
print()
print(f"Edsel Car Rental Company")
print(f"Customer Rental Recipt")
print()
print(f"Number of days rented:              {NumDays:>10d}")
print(":")
print(":")
print(f"Kilometers travelled:               {KMTrav:>10d}")

DailyChargeDsp = "${:,.2f}".format(DailyCharge)
print(f"Daily charge:                       {DailyChargeDsp:>10s}")
KMChargeDsp = "${:,.2f}".format(KMCharge)
print(f"Kilometer Charge:                  {KMChargeDsp:>10s}")
TotalChargeDsp = "${:,.2f}".format(TotalCharge)
print(f"Total Charge:                       {TotalChargeDsp:>10s}")

#Write the calues to a data file for storage.


# Any housekeeping duties at the end of the program. 