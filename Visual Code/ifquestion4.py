#Description: If Statement Question 4
# Author: Kassaundra Fequet
# Date(s): January 22/24
 
 
# Define required libraries.
 
 
 
# Define program constants.
SHIP_FEE = 1.15
LOCAL_FEE = 2.30
PROVINCE_FEE = 6.90
COUNTRY_FEE = 10.35
OTHER_FEE = 24.95
 
# Define program functions.
 
 
 
# Main program starts here.
 

   
# Gather user inputs.
PacKilo = input("Enter the weight of the package in kilograms: ")
PacKilo = float(PacKilo)
CusRegion = input("Enter the region: (L,P,C,O): ").upper()
 
 
# Perform required calculations.
if CusRegion == "L":
    RegionCost = LOCAL_FEE * PacKilo
    RegionName = "Local"
elif CusRegion == "P":
    RegionCost = PROVINCE_FEE * PacKilo
    RegionName = "Province"
elif CusRegion == "C":
    RegionCost = COUNTRY_FEE * PacKilo
    RegionName = "Country"
else:
    RegionCost = OTHER_FEE * PacKilo
    RegionName = "Other"

WeightCost = PacKilo * SHIP_FEE

TotalCost = RegionCost + WeightCost



# Display results
print()
print(f"Local Shipping Company")
print(f"Customer Shipping Receipt")
print()
print(f"Weight of package:        {PacKilo:>10.2f} kg")
print(f"Region:                   {RegionName:>10s}")



print()
WeightCostDsp = "${:,.2f}".format(WeightCost)
print(f"Weight Cost:               {WeightCostDsp:>10s}")
RegionCostDsp = "${:,.2f}".format(RegionCost)
print(f"Region Cost:               {RegionCostDsp:>10s}")
TotalCostDsp = "${:,.2f}".format(TotalCost)
print(f"Total Cost:                {TotalCostDsp:>10s}")


# Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.