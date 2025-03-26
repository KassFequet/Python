# Description: 
# Author: 
# Date(s): 


# Define required libraries.



# Define program constants.



# Define program functions.



# Main report processing starts here.


# Generate report headings.

# Initialize counters and accumulators.

# Open the data file. Places the cursor at the start of the first record.
f = open("Filename", "r")

# Process each line (record) in the file in a loop.
for XRecord in f:
 
    # The following line reads the first record in the file and creates a list.
    XLst = XRecord.split(",")
    
    # Now grab the values from the list and assign to variables. 
    # You may not need all the fields.
    EmpNum = XLst[0].strip()


    # Perform required calculations.


    # Display the detail line.

    
    # Update counters and accumulators.



# Close the file.
f.close()

# Print summary data - counters and accumulators.
