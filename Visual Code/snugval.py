# Description:Validations Snuggly Company
# Author: Class
# Date(s): Feb 3/25


# Define required libraries.



# Define program constants.



# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'")
    allowed_num = set("1234567890")
    allowed_char_num = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'1234567890")
    allowed_upper_char = ("ABCDEFGHIJKLMONPQRSTUVWXYZ")
    allowed_upper_char_num = set("ABCDEFGHIJKLMONPQRSTUVWXYZ1234567890")
    
    while True:
        CustName = input("Enter the customers name: ")
        if CustName =="":
            print()
            print(" Data Entry Error - Customer name must be entered.")
            print()
        elif set(CustName).issubset(allowed_char) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Customer Name contains invalid characters. Please re-enter.")
            print()
        else:
            break
        
    while True:
        StAdd = input("Enter the customer street address: ")
        if StAdd =="":
            print()
            print(" Data Entry Error - Street address must be entered.")
            print()
        elif set(StAdd).issubset(allowed_char_num) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Street address contains invalid characters. Please re-enter.")
            print()
        else:
            break

    while True:
        City = input("Enter the customer city: ")
        if City =="":
            print()
            print(" Data Entry Error - Customer city must be entered.")
            print()
        elif set(City).issubset(allowed_char) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Customer City contains invalid characters. Please re-enter.")
            print()
        else:
            break
        
    while True:
        Prov = input("Enter the customer province (XX): ").upper()
        if Prov =="":
            print()
            print(" Data Entry Error - Customer province must be entered.")
            print()
        elif len(Phone) != 2:
            print()
            print(" Data Entry Error = Province must contain 2 digits only. ")
            print()
        elif set(Prov).issubset(allowed_upper_char) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Customer province contains invalid characters. Please re-enter.")
            print()
        elif Prov != "NL" and Prov != "NS" and Prov != "PE" and Prov != "NB": #etc for rest of prov/terr
            print()
            print(" Data Entry Error = Customer province is not valid.")
            print()
        else:
            break
    
    while True:
        PostCode = input("Enter the customer postal code (X0X0X0): ").upper()
        if PostCode =="":
            print()
            print(" Data Entry Error - Customer postal code must be entered.")
            print()
        elif len(PostCode) != 6:
            print()
            print(" Data Entry Error = Postal code must contain 6 characters only. ")
            print()
        elif set(PostCode).issubset(allowed_upper_char_num) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Customer postal code contains invalid characters. Please re-enter.")
            print()
        else:
            break
        
    while True:
        Phone = input("Enter the customer phone number (0000000000): ")
        if Phone =="":
            print()
            print(" Data Entry Error - Customer phone number must be entered.")
            print()
        # Use the len() function to count the number of characters in a string
        elif len(Phone) != 10:
            print()
            print(" Data Entry Error = Phone number must contain 10 digits only. ")
            print()
        elif set(Phone).issubset(allowed_num) == False:
            # Every character in the name must be in the set of allowed characters.
            print()
            print(" Data Entry Error = Customer phone number contains invalid characters. Please re-enter.")
            print()
        else:
            break

    while True:
        try: #for numeric values.
            NumSnug = input("Enter the number of Snugglys ordered (1-20): ")
            NumSnug = int(NumSnug) #If this line causes an error, it goes to the excpet. If I try to convert to an integer and it cant iot gos to the except. If it can't do it that means the value is not an integer and invalid. 
        except:
            print()
            print("    Data entry error = Number of Snuggly's not a valid integer. ")
            print()
        else:
            #Value is valid, now checking the range
            if NumSnug <1 or NumSnug >20:
                print()
                print("    Data Entry error - Number of snuggly's must be between 1 and 20.")
                print()
            else:
                break

    while True:
        MethPay = input("Enter the method of payment (C)redit card or (P)ay later: ").upper()
        if MethPay =="":
            print()
            print("   Data Entry Error - Payment method cannot be blank")
        elif len(MethPay) != 1:
            print()
            print(" Data Entry Error = Method of payment must contain 1 character (C or P). ")
            print()
        elif MethPay != "C" and MethPay !="P":
            print()
            print("    Data entry error = Method of payment must be a C or a P")
            print()
        else:
            break
        
    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.