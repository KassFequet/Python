print()
TotRevMth = input("Enter the total revenue per month:          ")
TotRevMth = float(TotRevMth)
MorRentCost = input("Enter the cost of mortage/rent per month:   ")
MorRentCost = float(MorRentCost)
FoodCost = input("Enter the cost of food per month:           ")
FoodCost = float(FoodCost)
CloCost = input("Enter the cost of clothing per month:       ")
CloCost = float(CloCost)
EntCost = input("Enter the cost of entertainment per month:  ")
EntCost = float(EntCost)

print()
TotExpMth = MorRentCost + FoodCost + CloCost + EntCost
TotSavMth = TotRevMth - TotExpMth

print()
PerMorRentSpent = (MorRentCost / TotRevMth) *100
PerFoodSpent = (FoodCost / TotRevMth) * 100
PerCloSpent = (CloCost / TotRevMth) * 100
PerEntSpent = (EntCost / TotRevMth) * 100

print()
print("Total revenue per month:           ", TotRevMth)
print("Cost of mortgage/rent per month:   ", MorRentCost)
print("Cost of food per month:            ", FoodCost)
print("Cost of clothes per month:         ",CloCost)
print("Cost of entertainment per month:   ", EntCost)

print()
print("Total expenses per month:          ", TotExpMth)
print("Total savings per month:           ", TotSavMth)

print()
print("Percentage of monthly revenue spent on mortgage/rent: ", PerMorRentSpent)
print("Percentage of monthly revenue spent on food:          ", PerFoodSpent)
print("Percentage of monthly revenue spent on clothing:      ", PerCloSpent)
print("Percentage of monthly revenue spent on entertainemnt: ", PerEntSpent)