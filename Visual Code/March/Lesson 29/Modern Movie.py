# Description: Modern Movie - add movies to the Movies.dat file.
# Author: Mo and Class
# Date(s): March 18/25


# Define required libraries.
import FormatValues as FV
import sys
import time


# Define program constants.
MOVIE_ID = 10285


# Define program functions.



# Main program starts here.
while True:


    # Gather user inputs.
    print()
    MovieName = input("Enter the movie name (End to finish): ").title()
    if MovieName == "End":
        break
    
    MovieType = input("Enter the movie type (D, C, M, H): ").upper()
    MovieRating = input("Enter the movie rating (G, P, R): ").upper()
    RentalCost = input("Enter the rental cost (1.99 - 8.99): ")
    RentalCost = float(RentalCost)
    
    


    #Perform required calculations.



    # Display results



    # Write the values to a data file for storage.
    f = open("Movies.dat", "a")
    
    f.write(f"{str(MOVIE_ID)}, ") #FV.FNumber0(MOVIE_ID) would also make it a string
    f.write(f"{MovieName}, ")
    f.write(f"{MovieType}, ")
    f.write(f"{MovieRating}, ")
    f.write(f"{FV.FNumber2(RentalCost)}\n ")

    f.close()
    
    #print a simple message to let the user know that the data has been saved
    '''
    print()
    print("Movie " + MovieName + " has been successfully saved.")
    print()
    '''
    
    
    #Display a blinking message to let the user know that the data has been saved
    print()
    
    '''
    Message = "Saving Movie Data for " + MovieName + " ..."
    for _ in range(5): #Change to control no of blinks
        print(Message, end='\r')
        time.sleep(.3)
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)
        
    print()
    '''
    #Display a progress bar
    
    
    MOVIE_ID += 1
    


# Any housekeeping duties at the end of the program.