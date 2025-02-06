# Comment like a pro.
 
# Define variables - could have been input or calculations.
InvNo = 7485
InvDate ="25-01-14"
# 8 char - DD-MM-YY (US) or YY-MM-DD (CAN), 10 char - DD-MM-YYYY or YYYY-MM-DD
# 9 char - DD-Mon-YY, 29 char - Wednesday, September 30, 2025
 
CustName = "Christopher Wilson"
StAdd = "345 Newfoundland Dr."
City = "St. John's"
Prov = "NL"
Postal = "A1A9Y8"
 
PlateNum = "ABC123"
Mileage = 13758
 
CostLabor = 1248.00
CostParts = 1142.00
TotDis = 25.00
HST = 58.50
TotDue = 1243.50
 
# Display results as per printer spacing chart provided.
print()
print(f"                        HONEST PETER'S GARAGE")
print(f"                           123 Fixit Street")
print(f"                       St. John's, NL  A1A 1A1")
print(f"  Invoice #: {InvNo:>4d}                                     Date: {InvDate:<8s}")
print(f"  ------------------------------------------------------------------")
print(f"   Customer: {CustName:<30s}     Plate Number: {PlateNum:<6s}")
print(f"   Address:  {StAdd:<30s}     Mileage:      {Mileage:>6d}")
print(f"             {City:<18s}, {Prov:<2s}  {Postal:<6s} ")
print()  
 
CostLaborDsp = "${:,.2f}".format(CostLabor)
print(f"                                           Cost of Labor:  {CostLaborDsp:>9s}")
 
CostPartsDsp = "${:,.2f}".format(CostParts)
print(f"                                           Cost of parts:  {CostPartsDsp:>9s}")
 
TotDisDsp = "${:,.2f}".format(TotDis)
print(f"                                          Total Discount:  {TotDisDsp:>9s}")
 
HSTDsp = "${:,.2f}".format(HST)
print(f"                                                     HST:  {HSTDsp:>9s}")
 
print(f"                                                           ---------")
 
TotDueDsp = "${:,.2f}".format(TotDue)
print(f"                                           Invoice Total:  {TotDueDsp:<19s}")
print(f"  ------------------------------------------------------------------")
print(f"      Honest Peter's - There to meet the needs of our customers!!")
print(f"  ------------------------------------------------------------------")