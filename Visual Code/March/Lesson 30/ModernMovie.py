# Description: Add movies to the Movies.dat file.
# Author: Maurice & SD 14
# Date(s): March 18/25 -
 
 
# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time
 
 
# Define program constants.
# Open the defaults file and read the values into variables
f = open('MMDefaults.dat', 'r')
MOVIE_ID = int(f.readline())
HST_RATE = float(f.readline())
DAYS_NR = int(f.readline())
OBS_WKS = int(f.readline())
f.close()
 
 
# Define program functions.
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
 
 
# Main program starts here.
while True:
   
    # Gather user inputs.
    print()
    MovieName = input("Enter the movie name (End to finish): ").title()
    if MovieName == "End":
        break
    RelDate = input("Enter the release date (YYYY-MM-DD): ")
    RelDate = datetime.datetime.strptime(RelDate, "%Y-%m-%d")
 
    MovieType = input("Enter the movie type (D, C, M, H): ").upper()
    MovieRating = input("Enter the movie rating (G, P, R): ").upper()
    RentalCost = input("Enter the rental cost (1.99 - 8.99): ")
    RentalCost = float(RentalCost)
 
 
    # Perform required calculations.
    HST = RentalCost * HST_RATE
    TotRentCost = RentalCost + HST
 
    NewRelEndDate = RelDate + datetime.timedelta(days=DAYS_NR)
    ObsDate = RelDate + datetime.timedelta(weeks=OBS_WKS)
 
 
    # Display results
    print(f"Rental cost:              {FV.FDollar2(RentalCost):>9s}")
    print(f"HST:                      {FV.FDollar2(HST):>9s}")
    print(f"Total rental cost:        {FV.FDollar2(TotRentCost):>9s}")
    print()
    print(f"Release date:             {FV.FDateM(RelDate):>9s}")
    print(f"New release end date:     {FV.FDateM(NewRelEndDate):>9s}")
    print(f"Obselescence date:        {FV.FDateM(ObsDate)}")
 
 
    # Write the values to a data file for storage.
    f = open("Movies.dat", "a")
 
    f.write(f"{str(MOVIE_ID)}, ") # FV.FNumber0(MOVIE_ID)
    f.write(f"{FV.FDateM(RelDate)}, ")
    f.write(f"{MovieName}, ")
    f.write(f"{MovieType}, ")
    f.write(f"{MovieRating}, ")
    f.write(f"{FV.FNumber2(RentalCost)}, ")
    f.write(f"{FV.FDateM(NewRelEndDate)}, ")
    f.write(f"{FV.FDateM(ObsDate)}\n")
 
    f.close()
 
    # Print a simple message to let the user know the data is saved.
 
    # Display a Progress Bar to let the user know data is saved.
    print()
 
    TotalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Movie Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()
    print("Movie information for " + MovieName + " successfully saved.")
    print()
 
    # Update any values for the next process through the loop.
    MOVIE_ID += 1
 
    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.
    f = open('MMDefaults.dat', 'w')
 
    f.write(f"{MOVIE_ID}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{DAYS_NR}\n")
    f.write(f"{OBS_WKS}\n")
   
    f.close()
 
 
# Any housekeeping duties at the end of the program.
# OR write the defualts back to the file here.