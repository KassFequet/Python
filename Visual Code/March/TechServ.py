# Description: Process a receipt for customer purchases from Tech Services Inc.
# Author: Maurice & SD 14
# Date(s): March 12/25 - March 13-25


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.
CUR_DATE = datetime.datetime.now()
INV_NUM = 10367


# Define program functions.
def GetPayDue(InvoiceDate):
    # Determine the payment date based on 20 days after the invoice date
    # or the first day of the next month - whichever is later.

    Pay20Date = InvoiceDate + datetime.timedelta(days=20)
    PurYear = InvoiceDate.year
    PurMonth = InvoiceDate.month
    PurDay = InvoiceDate.day

    PayYear = PurYear
    PayMonth = PurMonth + 1
    if PayMonth == 13:
        PayMonth -= 12
        PayYear += 1
    PayDay = 1
    PayFirstDate = datetime.datetime(PayYear, PayMonth, PayDay)

    if Pay20Date > PayFirstDate:
        PayDate = Pay20Date
    else:
        PayDate = PayFirstDate

    return PayDate


# Main program starts here.
while True:
    
    # Gather user inputs.
    CustName = input("Enter the customer name: ")
    PhoneNum = input("Enter the customer pbine number (9999999999): ")

    DescLst = []
    PriceLst = []
    QtyLst = []
    SubtotalLst = []
    while True:
        print()
        Desc = input("Enter the item description (End to finish): ").title()
        if Desc == "End":
            break
        Price = input("Enter the retail price of the item: ")
        Price = float(Price)
        Qty = input("Enter the quantity purchased: ")
        Qty = int(Qty)

        Subtotal = Price * Qty

        DescLst.append(Desc)
        PriceLst.append(Price)
        QtyLst.append(Qty)
        SubtotalLst.append(Subtotal)

    PayLst = ["Cash", "Debit", "Visa", "Mastercard"]
    while True:
        PayMethod = input("Enter the payment method (Cash, Debit, Visa, Mastercard): ").title()

        if PayMethod not in PayLst:
            print()
            print("    Data Entry Error - Payment method is invalid.")
            print()
        else:
            break


    # Perform required calculations.
    TotalItemsOrdered = len(Desc)
    TotalSubtotal = sum(SubtotalLst)

    PayDueDate = GetPayDue(CUR_DATE)
    

    # Display results
    print()
    print(f"Tech Services Inc.                            Invoice No:       {INV_NUM:>5d}")
    print(f"Customer Invoice                              Invoice Date: {FV.FDateM(CUR_DATE)}")
    # Short date - YYYY-MM-DD, Medium Date - dd-MON-yy, Long date is Day, Month, dd, yyyy

    print()
    print(f"Customer: {CustName:<20s}  {FV.FPhone14(PhoneNum)}")
    print()

    print(f"Item Description          Item Price   Quantity Purchased    Subtotal")
    print(f"---------------------------------------------------------------------")

    # If you are working with only one list - use "for Value in ListLst:".
    # With multiple lists, set up an index starting at 0, and process each index to the end.

    for i in range(0, len(DescLst)):
        print(f"{DescLst[i]:<20s}       {FV.FDollar2(PriceLst[i]):>7s}           {QtyLst[i]:>2d}             {FV.FDollar2(SubtotalLst[i]):>9s}")

    print(f"---------------------------------------------------------------------")
    print(f"Total items / services ordered: {TotalItemsOrdered:>2d}                         {FV.FDollar2(TotalSubtotal):>10s}")
    print()
    print(f"Payment Method: {PayMethod:<10s}                     Payment Due: {FV.FDateM(PayDueDate):>9s}")


    # Write the values to a data file for storage.

    # Use the simplest form of a file - comma separated text file.
    # Each line (record) will be stored with comma separators.  For example:
    #    Value, Value, Value, Value, Value, Value, Value
    # Each record will contain the same number of fields (Values) in the same order.

    # To add data to a file.

    # Step 1 - create a connection to the file by opening it.
    # Step 2 - process the data IE: Write the record to the file, Read the record from a file.
    #        - This part is sometimes in a loop - especially when you read.
    # Step 3 - destroy the connection by closing the file.


    Continue = input("Do you want to process another order (Y / N): ").upper()
    if Continue == "N":
        break

# Any housekeeping duties at the end of the program.
