# Description: QAP #2 - St. Johns Marina & Yacht Club
# Author: Kassaundra Fequet
# Date(s): January 27/25 - February 1/25



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
Date = input("Enter the current date(YYYYMMDD):          ")
SiteNum = input("Enter the site number (1-100):             ")
SiteNum = int(SiteNum)

print()
MemName = input("Enter the members name:                    ")
StAdd = input("Enter the street address:                  ")
City = input("Enter the city:                            ")
Prov = input("Enter the province (XX):                   ")
PostCode = input("Enter the postal code (X0X0X0):            ")

print()
HomePhone = input("Enter the home phone number (0000000000):  ")
CellPhone = input("Enter the cell phone number (0000000000):  ")

print()
MemType = input("Enter the membership type (S/E):           ").upper()
NumAltMembers = input("Enter the number of alternate members:     ") #Family and friends that are allowed to access the grounds.
NumAltMembers = int(NumAltMembers)
Clean = input("Do you want weekly site cleaning? (Y/N):   ").upper()
Video = input("Do you want video surveillance? (Y/N):     ").upper()

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
print(f" St. John's Marina & Yacht Club")
print(f"      Yearly Member Receipt")
print()
print(f"---------------------------------")
print()
print(f"Client Name and Address: ")
print()
print(f"         {MemName:>24s}")
print(f"         {StAdd:>24s}")
print(f"       {City:>15s}, {Prov:>2s} {PostCode:>6s}")
print()
print(f"Phone: {HomePhone:<10s} (H)")
print(f"       {CellPhone:<10s} (C)")
print()
print(f"Site #: {SiteNum:<3d} Member type: {MemTypeName:<9s}")
print()
print(f"Alternate members:             {NumAltMembers:>2d}")
print(f"Weekly site cleaning:         {CleanAns:>3s}")
print(f"Video surveillance:           {VideoAns:>3s}")
print()
SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print(f"Site charges:           {SiteChargeDsp:>9s}")
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
print(f"Extra charges:            {ExtraChargeDsp:>7s}")
print(f"                    -------------")
SubtotalDsp = "${:,.2f}".format(Subtotal)
print(f"Subtotal:               {SubtotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"Sales tax(HST):           {HSTDsp:>7s}")
print(f"                   --------------")
TotMonChargeDsp = "${:,.2f}".format(TotMonCharge)
print(f"Total monthly charges:  {TotMonChargeDsp:>9s}")
MonDuesDsp = "${:,.2f}".format(MonDues)
print(f"Monthly dues:             {MonDuesDsp:>7s}")
print(f"                    -------------")
TotMonFeeDsp = "${:,.2f}".format(TotMonFee)
print(f"Total monthly fees:     {TotMonFeeDsp:>9s}")
TotYearFeeDsp = "${:,.2f}".format(TotYearFee)
print(f"Total yearly fees:    1234 {TotYearFeeDsp:>10s}")
print()
MonPayDsp = "${:,.2f}".format(MonPay)
print(f"Monthly payment:        {MonPayDsp:>9s}")
print()
print(f"---------------------------------")
print()
print(f"Issued: {Date:<8s}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()
CanFeeDsp = "${:,.2f}".format(CanFee)
print(f"Cancellation fee:      {CanFeeDsp:>9s}")
print()

# Write the values to a data file for storage.


# Any housekeeping duties at the end of the program.