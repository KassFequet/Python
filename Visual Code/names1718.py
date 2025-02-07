
FirstName ="John"
LastName = "Doe"
Title = "Mr"

print(f"{Title:<4s} {FirstName:<15s} {LastName:<15s}")

# Add the elements of the name into a single variable.
# using a process called concatenation - adding strings to the end of strings

FullName = Title + " " + FirstName + " " + LastName    #The " " is adding a space in between the variables.

print(f"{FullName:<35s}") #Add the amount for each string (15 + 15 + 4) rounded to 35 just to make it cleaner to read.

# as a string is placed in memory, each character is defined with an index, starting at 0.

Initial = FirstName[0] #This specifies what element is wanted, so in this case the first element aka the J.
print(Initial)
FirstTwo = LastName[0:2] #This gives a range of what is wanted. So this is the first 2 letters in the name. Once it gets to the second # it finishes so you always have to add 1 to  the end. It stops at the last element #.
print(FirstTwo)


print(f"{Initial:<1s}. {LastName:<15s}")
#If you get extra spacing, consider concatenation.
FullName = Initial + ". " + LastName
print(f"{FullName:<18s}")
