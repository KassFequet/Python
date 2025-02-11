ItemName = input("Enter the item name: ")
ItemCost = input("Enter the item cost: ")
ItemCost = float(ItemCost)
NumInStock = input("Enter the number of items in stock: ")
NumInStock = int(NumInStock)

Markup = ItemCost * .75 
RetailPrice = ItemCost + Markup

TotInvCost = ItemCost * NumInStock 
TotInvRetail = RetailPrice * NumInStock 
GrossMargin = TotInvRetail - TotInvCost 

Sale10Off = RetailPrice * .90 
Sale25Off = RetailPrice * .75 
Sale33Off = RetailPrice * .67 
Sale50Off = RetailPrice * .50

print(ItemName)
print(ItemCost)
print(NumInStock)

print(RetailPrice)
print(TotInvCost)
print(TotInvRetail)
print(GrossMargin)

print(Sale10Off)
print(Sale25Off)
print(Sale33Off)
print(Sale50Off)
