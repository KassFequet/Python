# Comment like a pro.
 
#Define program constants.
HST_RATE = .15
# Values that were input or calculated.
DateProcessed = "01-06-25"
SalesPerson = "Billy Joe McAllister"
Location = "Montreal"
StartDate = "12-15-25"
EndDate = "12-22-25"
NumDays = 7
DayCharge = 658.56
Mileage = 546
MilCharge = 132.54
HST = 102.84
ClaimTotal = 893.94
 
# Display program results.
print()
print(f"              ABC COMPANY")
print(f"       CLAIM CONFIRMATION RECEIPT")
print()
print(f"   Date processed: {DateProcessed:<8s}")
print(f"   Salesperson:    {SalesPerson:<20s}")
print(f"   Location:       {Location:<20s}")
print(f"   Dates:          {StartDate:<8s} to {EndDate:<8s}")
print(f"   ------------------------------------")
 
DayChargeDsp = "${:,.2f}".format(DayCharge)
print(f"   Days:     {NumDays:>3d}   Charge:    {DayChargeDsp:>9s}")

MilChargeDsp = "${:,.2f}".format(MilCharge)
print(f"   Mileage:   {Mileage:>4d}            {MilChargeDsp:>9s}")

HST_RATEDsp = "{:.0%}".format(HST_RATE)
HSTDsp = "${:,.2f}".format(HST)
print(f"   Tax (HST @{HST_RATEDsp:>3s}):            {HSTDsp:>9s}")       
print(f"                              ---------")    

ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
print(f"   Claim total:               {ClaimTotalDsp:>9s}")                                   
                                                