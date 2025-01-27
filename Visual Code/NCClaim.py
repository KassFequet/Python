print()
SalesName = input("Enter the salesperson name:     ")
TripLoc =   input("Enter the trip location:        ")
print()
NumDays =   input("Enter the number of days:       ")
NumDays = int(NumDays)
NumKilos =  input("Enter the number of kilometres: ")
NumKilos = int(NumKilos)

print()
PerDiemAmt = NumDays * 56.00
NumNights = NumDays - 1 
LodgeAmt = NumNights * 125.00 
MilAmt = NumKilos * .24 
TotalClaim = PerDiemAmt + LodgeAmt + MilAmt 

print()
TaxAmt = PerDiemAmt + LodgeAmt 
HST = TaxAmt * .15 
ClaimTotal = TotalClaim + HST

print()
print("Salesperson Name:     ", SalesName)
print("Trip Location:        ", TripLoc)
print("Number of Days:       ", NumDays)
print("Number of Kilometres: ", NumKilos)

print()
print("Per Diem Amount:      ", PerDiemAmt)
print("Lodgeing Amount:      ",   LodgeAmt)
print("Mileage Amount:       ",      MilAmt)

print()
print("Total Claim Amount:   ", TotalClaim)
print("HST:                  ", HST)
print("Claim Total:          ", ClaimTotal)