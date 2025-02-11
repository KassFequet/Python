#Descriptions: Determine total invoice for Edsel Car Rental Company service.
#Author: Kassaundra Fequet
#Date: January 15/2025

# Constants
PER_DAY_RATE = 75.00 # Automobiles are rented for $75.00 per day.
PER_KM_RATE = 0.16 # Automobiles are rented at .16 cents per kilometer traveled.

INS_DAY_RATE = 19.00 # Insurance is applied at $19.00 per day.
RENT_COST_DIS_RATE= .10 # Winter discount rate of 10% off the rental cost. 
MIL_COST_DIS_RATE = .25 # Winter discount rate of 25% off the mileage cost.

HST_RATE = .15 #Current rate to calcualet the HST

# User input
print()
CustName = input("Enter the customer name:                                   ")
CustPhone = input("Enter the customer phone number:                           ")

print()
NumDays = input("Enter the number of days the automobile was rented:        ")
NumDays = int(NumDays)

print()
OdoRent = input("Enter the odometer reading when the automobile was rented: ")
OdoRent = int(OdoRent)
OdoReturn = input("Enter the odometer when the automobile was returned:       ")
OdoReturn = int(OdoReturn)

#Calculations
TotalKm = OdoReturn - OdoRent 

RentCost = NumDays  * PER_DAY_RATE 
MilCost = TotalKm * PER_KM_RATE 
InsCost = NumDays * INS_DAY_RATE 

RentCostDis = RentCost * RENT_COST_DIS_RATE 
MilCostDis = MilCost * MIL_COST_DIS_RATE 
TotalDis = RentCostDis + MilCostDis 

TotalRentCost = (RentCost + MilCost + InsCost) - TotalDis
HST = TotalRentCost * HST_RATE 
FinInvTotal = TotalRentCost + HST 

# User results.
print()
print("Customer name:                                  ", CustName)
print("Customer phone number:                          ", CustPhone)

print()
print("Number of days the automobile was rented:       ", NumDays)

print()
print("Odometer reading when automobile was rented:    ", OdoRent)
print("Odometer reading when automobile was returned:  ", OdoReturn)
print("Total kilometers driven:                        ", TotalKm )

print()
print("Rental cost:                                    ", RentCost)
print("Mileage cost:                                   ", MilCost)
print("Insurance cost:                                 ", InsCost)

print()
print("Total discount:                                 ", TotalDis)
print("Total rental cost:                              ", TotalRentCost)
print("HST:                                            ", HST)

print()
print("Invoice total:                                  ", FinInvTotal)