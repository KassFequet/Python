

#Define variables - could have input or calculation
InvNo = 7485
InvDate ="25-01-14"

CustName = "Christopher Wilson"
StAdd = "345 Newfoundland Dr"
City = "St. John's"
Prov = "NL"
Postal = "A1A9Y8"

PlateNum = "ABC123"
Mileage = 13758

CostLabor = 248.00
CostParts =  142.00
TotalDis = 25.00
HST = 58.50
TotDue = 423.50




print()
print(f"                      HONEST PETER'S GARAGE")
print(f"                         123 fixit Street")
print(f"                     St. John's, NL, A1A 1A1")
print(f"   Invoice #: {InvNo:>4d}               Date: {InvDate:>8s}")
print(f"  --------------------------------------------------  ")
print(f"   Customer: {CustName:<30s}     Plate Number{PlateNum:<6s}")
print(f"   Address:  {StAdd:<30s}     Mileage:      {Mileage:>6d}")
print()

CostLaborDsp = "${:,.2f}".format(CostLabor)
print(f"                                                  Cost of Labor:  {CostLaborDsp:>9s}")

CostPartsDsp = "${:,.2f}".format(CostParts)
print(f"                                                  Cost of Parts:  {CostPartsDsp:>9s}")

TotDisDsp = "${:,.2f}".format(TotalDis)
print(f"                                                 Total discount:     {TotDisDsp:>9s}")

HSTDsp = "${:,.2f}".format(HST)
print(f"                                                            HST:           {HST:>9s}")

print(f"                                                            ---------")

TotDueDsp = "${:,.2f}".format(TotDue)
print(f"                                                   Invoice Total:    {TotDueDsp:>9s}")
print(f" -------------------------------------------------------------------------------")
print(f"        Honest Peter's - There to meet the needs of our customer!!        ")
print(f"  ------------------------------------------------------------------------------")