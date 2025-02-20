# Description: 
# Author: Kassaundra Fequet
# Date(s): February 18/2025 - 

#Generate email address - done
#Generate email password - done 
#Email signature 
#generate witch name
#Determine Zodiac sign - done but no horoscope
#Compnay witch veteran status - done

# Define required libraries.
import datetime
import random


# Define program constants.
CUR_DATE = datetime.datetime.now()
DOMAIN = "@CelestialSorcery.com"


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    print()
    print("Welcome to Celestial Sorcery - A Coven Forged in Darkness and Bound by The Stars")
    print()

    while True:
        FirstName = input("Enter the employee's first name: ")

        if FirstName == "":
            print()
            print("   Data Entry Error - First name must be entered")
            print()
        else:
            break

    while True:
        LastName = input("Enter the employee's last name: ")

        if LastName == "":
            print()
            print("   Data Entry Error - Last name must be entered")
            print()
        else:
            break

    while True:
        PhoneNum = input("Enter the employee's phone number (0000000000):")
        
        if PhoneNum == "":
            print()
            print("   Data Entry Error - Phone number must be entered.")
            print()
        elif len(PhoneNum) != 10:
            print()
            print("   Data Entry Error - Phone number must contain 10 digits only")
            print()
        elif PhoneNum.isdigit() == False:
            print()
            print("   Data Entry Error - Phone number contains invalid characters")
            print()
        else:
            break

    while True:
        try:
            StartDate = input("Enter the start date (YYYY-MM-DD): ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print(" Error - date is invalid - use YYYY-MM-DD format")
        else:
            if StartDate > CUR_DATE:
                print("  Error - cannot enter a date in the future")
            else:
                break

    while True:
        try:
            BirthDate = input("Enter the birth date (YYYY-MM-DD): ")
            BirthDate = datetime.datetime.strptime(BirthDate, "%Y-%m-%d")
        except:
            print(" Error - date is invalid - use YYYY-MM-DD format")
        else:
            if BirthDate > CUR_DATE:
                print("  Error - cannot enter a date in the future")
            if BirthDate > StartDate:
                print("  Error - cannot enter a birth date after the start date")
            else:
                break


    # Perform required calculations.

    Email = (FirstName.title()) + "." + (LastName.title()) + DOMAIN

    Password = (LastName[0:3]) + (FirstName[0:3]) + (str(random.randint(1000, 9999)))

    # Calculations to determine the zodiac sign of employee
    if datetime.datetime(BirthDate.year, 12, 22) <= BirthDate <= datetime.datetime(BirthDate.year, 1, 19):
        Zodiac = "Capricorn"
    elif datetime.datetime(BirthDate.year, 1, 20) <= BirthDate <= datetime.datetime(BirthDate.year, 2, 18):
        Zodiac = "Aquarius"
    elif datetime.datetime(BirthDate.year, 2, 19) <= BirthDate <= datetime.datetime(BirthDate.year, 3, 20):
        Zodiac = "Pisces"
    elif datetime.datetime(BirthDate.year, 3, 21) <= BirthDate <= datetime.datetime(BirthDate.year, 4, 19):
        Zodiac = "Aries"
    elif datetime.datetime(BirthDate.year, 4, 20) <= BirthDate <= datetime.datetime(BirthDate.year, 5, 20):
        Zodiac = "Taurus"
    elif datetime.datetime(BirthDate.year, 5, 21) <= BirthDate <= datetime.datetime(BirthDate.year, 6, 20):
        Zodiac = "Gemini"
    elif datetime.datetime(BirthDate.year, 6, 21) <= BirthDate <= datetime.datetime(BirthDate.year, 7, 22):
        Zodiac = "Cancer"
    elif datetime.datetime(BirthDate.year, 7, 23) <= BirthDate <= datetime.datetime(BirthDate.year, 8, 22):
        Zodiac = "Leo"
    elif datetime.datetime(BirthDate.year, 8, 23) <= BirthDate <= datetime.datetime(BirthDate.year, 9, 22):
        Zodiac = "Virgo"
    elif datetime.datetime(BirthDate.year, 9, 23) <= BirthDate <= datetime.datetime(BirthDate.year, 10, 22):
        Zodiac = "Libra"
    elif datetime.datetime(BirthDate.year, 10, 23) <= BirthDate <= datetime.datetime(BirthDate.year, 11, 21):
        Zodiac = "Scorpio"
    elif datetime.datetime(BirthDate.year, 11, 22) <= BirthDate <= datetime.datetime(BirthDate.year, 12, 21):
        Zodiac = "Sagittarius"
    else:
        Zodiac = "Capricorn" #Due to Capricorn being in between years it is added as else


    # Calculations to determine veteran status of employee
    YearsWorked = (CUR_DATE - StartDate).days / 365

    if YearsWorked <=1: 
        Status = "Nebula Novice"
    elif YearsWorked <=5:
        Status = "Experienced Stargazer"
    elif YearsWorked <=10:
        Status = "Celestial Senior"
    else:
        Status = "Astral Veteran"

    # Calcluations for email signaure
    PhoneNumDsp = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    FullName = (FirstName.title()) + " " + (LastName.title())

    EmailSig = (FullName) + " | " + (Status) + " | " + (PhoneNumDsp) + " | " + (Email)

    # Display results
    print()
    print(f"Email Address: {Email}")
    print(f"Email Password: {Password}")
    print(f"Zodiac Sign: {Zodiac}")
    print(f"Employee Status: {Status}")
    print(f"Email Signature: {EmailSig}")


    # Write the values to a data file for storage.


    
# Any housekeeping duties at the end of the program.