# Description: QAP #2 - St. Johns Marina & Yacht Club
# Author: Kassaundra Fequet
# Date(s): January 27/24 -



# Define required libraries.



# Define program constants.
EVEN_SITE_RATE = 80.00 #Even numbered sites cost $80/month.
ODD_SITE_RATE = 120.00 #Odd numbered sites cost $120/month.
ALT_MEM_RATE = 5.00 #Each alternate member costs $5/month.

CLEAN_RATE = 50.00 #Weekly site cleaning costs $50/month.
VIDEO_RATE = 35.00 #Video surveillance costs $35/month.

HST_RATE = .15 #The current HST rate is 15%.

STAN_MONTH_RATE = 75.00 #Standard members have a monthly dues rate of $75/month.
EXEC_MONTH_RATE = 150.00 #Executive members have a monthly dues rate of $150/month.

PROC_RATE = 59.99 #The processing fee is $59.99.
CAN_RATE = .60 #The cancellation fee is 60% of the yearly site charges.

# Define program functions.



# Main program starts here.



# Gather user inputs.

print()
Date = input("Enter the current date(YYYY-MM-DD): ")
SiteNum = input("Enter the site number (1-100): ")
SiteNum = int(SiteNum)

print()
MemName = input("Enter the members name: ")
StAdd = input("Enter the street address: ")
City = input("Enter the city: ")
Prov = input("Enter the province (XX): ")
PostCode = input("Enter the postal code (X0X0X0): ")

print()
HomePhone = input("Enter the home phone number (000-000-0000): ")
CellPhone = input("Enter the cell phone number (000-000-0000): ")

print()
MemType = input("Enter the membership type (S/E): ").upper()
NumAltMembers = input("Enter the number of alternate members: ") #Family and friends that are allowed to access the grounds.
NumAltMembers = int(NumAltMembers)
Clean = input("Do you want weekly site cleaning? (Y/N): ").upper()
Video = input("Do you want video surveillance? (Y/N): ").upper()

# Perform required calculations.

if SiteNum % 2 == 0:
    NumSiteCharge = EVEN_SITE_RATE
else:
    NumSiteCharge = ODD_SITE_RATE

AltMemCharge = ALT_MEM_RATE * NumAltMembers
SiteCharge = NumSiteCharge * AltMemCharge

if Clean =="Y":
    CleanCharge = CLEAN_RATE
    CleanAns = "Yes"
else:
    CleanCharge = 0
    CleanAns = "No"

if Video =="Y":
    VideoCharge = VIDEO_RATE
    VideoAns = "Yes"
else:
    VideoCharge = 0
    VideoAns = "No"

ExtraCharge = CleanCharge + VideoCharge
Subtotal = SiteCharge + ExtraCharge
HST = Subtotal * HST_RATE
TotMonCharge = Subtotal + HST

if MemType == "S":
    MonDues = STAN_MONTH_RATE
    MemTypeName = "Standard"
else:
    MonDues = EXEC_MONTH_RATE
    MemTypeName = "Executive"

TotMonFee = TotMonCharge + MonDues

#In the 3 following calculations, 12 represents the amount of months per year.
TotYearFee = TotMonFee * 12
MonPay = (TotYearFee + PROC_RATE) / 12
CanFee = (SiteCharge * 12) * CAN_RATE




# Display results
print()
print(f"St. John's Marina & Yacht Club")
print(f"Yearly Member Receipt")
print()
print(f"--------------------------------------------")
print()
print(f" Client Name and Address: ")
print()
print(f" {MemName:<24s}   ")
print(f" {StAdd:<24s}    ")
print(f" {City:<15s}, {Prov:<2s}, {PostCode:<6s} ")
print()
print(f"Phone: {HomePhone:<10s} (H)")
print(f"       {CellPhone:<10s} (C)")
print()
print(f"Site #:{SiteNum:<3d}: Member type: {MemTypeName:<}")
print()
print(f"Alternate members: {NumAltMembers:>2d}")
print(f"Weekly site cleaning: {CleanAns:>3s}")
print(f"Video surveillance: {VideoAns:>3s}")
print()
SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print(f"Site charges: {SiteChargeDsp:<6s}  ")
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
print(f"Extra charges: {ExtraChargeDsp:<5s} ")


# Write the values to a data file for storage.


# Any housekeeping duties at the end of the program.
'''
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
print(f"                                           Invoice Total:  {TotDueDsp:>9s}")
print(f"  ------------------------------------------------------------------")
print(f"      Honest Peter's - There to meet the needs of our customers!!")
print(f"  ------------------------------------------------------------------")
'''