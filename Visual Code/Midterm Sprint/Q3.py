# Description:  Midterm Sprint - Questions 3 - Celestial Sorcery Employee Overview
# Author: Kassaundra Fequet
# Date(s): February 18/2025 -  February 20/2025

# Define required libraries.
import datetime
import random


# Define program constants.
CUR_DATE = datetime.datetime.now()
DOMAIN = "@CelestialSorcery.com"


# Define program functions.



# Main program starts here.

#I added some basic validations to ensure that the user enters the correct information
while True:


    # Gather user inputs.
    print()
    print("Welcome to Celestial Sorcery - A Coven Forged in Darkness and Bound by The Stars")
    print()

    while True:
        FirstName = input("Enter the employee's first name:                ")

        if FirstName == "":
            print()
            print("   Data Entry Error - First name must be entered")
            print()
        else:
            break

    while True:
        LastName = input("Enter the employee's last name:                 ")

        if LastName == "":
            print()
            print("   Data Entry Error - Last name must be entered")
            print()
        else:
            break

    while True:
        PhoneNum = input("Enter the employee's phone number (0000000000): ")
        
        if PhoneNum == "":
            print()
            print("   Data Entry Error - Phone number must be entered")
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
            StartDate = input("Enter the start date (YYYY-MM-DD):              ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print()
            print("   Data Entry Error - Must use YYYY-MM-DD format")
            print()
        else:
            if StartDate > CUR_DATE:
                print()
                print("   Data Entry Error - Cannot enter a date in the future")
                print()
            else:
                break

    while True:
        try:
            BirthDate = input("Enter the birth date (YYYY-MM-DD):              ")
            BirthDate = datetime.datetime.strptime(BirthDate, "%Y-%m-%d")
        except:
            print()
            print("   Data Entry Error - Must use YYYY-MM-DD format")
            print()
        else:
            if BirthDate > CUR_DATE:
                print()
                print("   Data Entry Error - Cannot enter a date in the future")
                print()
            if BirthDate > StartDate:
                print()
                print("   Data Entry Error - Cannot enter a birth date after the start date")
                print()
            else:
                break

    # Perform required calculations.

    # Calculations to determine email address and password of employee
    Email = (FirstName.title()) + "." + (LastName.title()) + DOMAIN

    Password = (LastName[0:3]) + (FirstName[0:3]) + (str(random.randint(1000, 9999)))

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

    # Calculations for email signature
    PhoneNumDsp = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    FullName = (FirstName.title()) + " " + (LastName.title())

    EmailSig = (FullName) + " | " + (Status) + " | " + (PhoneNumDsp) + " | " + (Email)
    
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
        Zodiac = "Capricorn" #Due to Capricorn being between years it is added here for when it does not fit in the equations
        
    #Calculations to determine horoscope of employee
    if Zodiac == "Capricorn":
        Horoscope = "Like a distant star, your persistence may go unnoticed at first, but in time, your brilliance will illuminate the sky."
    elif Zodiac == "Aquarius":
        Horoscope = "Your mind is a nebula of innovation, shaping the future with cosmic vision."
    elif Zodiac == "Pisces":
        Horoscope = "You drift through the universe like a dream, finding magic in the unseen."
    elif Zodiac == "Aries":
        Horoscope = "Like a solar flare, your energy is powerful. Just be sure to pace yourself before burning out."
    elif Zodiac == "Taurus":
        Horoscope = "You are the cosmic anchor in a swirling universe, steady and unwavering in your path."
    elif Zodiac == "Gemini":
        Horoscope = "The stars whisper secrets to you. Stay open to messages that lead to new discoveries."
    elif Zodiac == "Cancer":
        Horoscope = "Your emotions ebb and flow like lunar tides, guiding you toward deeper understanding."
    elif Zodiac == "Leo":
        Horoscope = "You shine like a supernova, but true brilliance comes from the fire within."
    elif Zodiac == "Virgo":
        Horoscope = "Precision is your power, allowing you to map the stars of your own destiny."
    elif Zodiac == "Libra":
        Horoscope = "Like planets in perfect orbit, balance and harmony keep your world spinning smoothly."
    elif Zodiac == "Scorpio":
        Horoscope = "You are a black hole of mystery, drawing others in with your depth and intensity"
    else:
        Zodiac == "Sagittarius"
        Horoscope = "Like a comet, you blaze forward, meant to chase adventure, not stand still."

    # Display results
    print()
    print(f"Celestial Sorcery Employee Overview")
    print(f"-----------------------------------")
    
    print()
    print(f"Employee Status: {Status}")
    
    print()
    print(f"Email Address:   {Email}")
    print(f"Email Password:  {Password}")
    print(f"Email Signature: {EmailSig}")
    
    print()
    print(f"Zodiac Sign:     {Zodiac}")
    print(f"Horoscope:       {Horoscope}")
    print()



    # Write the values to a data file for storage.


    
# Any housekeeping duties at the end of the program.