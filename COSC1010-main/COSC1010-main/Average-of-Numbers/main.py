#
# Carmen Grajeda
# 10/16/2024
# Average of Numbers Programming Project
# COSC 1010 NT
#
# This program opens the file numbers.txt 
# and calculates the average of all the numbers.

# Constant Variable
infile = "numbers.txt" # The file containing a series of integers

# Local Variables
total = 0.0 # The variable to Initialize the accumulator
numbers = 0.0 # The variable for the value of the numbers
counter = 0 # The variable to initialize a count of the numbers

# Define the main function
def main():
    # Initialize an accumulator.
    total = 0.0
    # Initialize a variable to keep count of the numbers.
    counter = 0

    try: # exception handler
        # Open the numbers.txt file.
        infile = open('numbers.txt', 'r')
        # Read the numbers from the file
        # and accumulate them.
        for line in infile:
            number = float(line)
            total += number 
            #Add 1 to the counter.
            counter = counter + 1 

        # Close the file. 
        infile.close()

        # Calculate the average of all the numbers stored in the file. 
        if counter > 0: 
            average = total / counter
            # Display the average of the numbers.
            print(f"The average of the numbers in '{infile}' is: {average}")
        else: # If there is no data in the file.
            print(f"The file '{infile}' is empty.")
    
    # Write except clause to catch any exception that is raised in the try suite.
    except IOError:
        # Display the except clause IOError.
        print('An error occurred while trying to read the file.')
    except ValueError:
        # Display the except clause for ValueError.
        print('Non-numeric data found in the file.')
        # Display the except clause in line 30.
    except:
        print('An error occurred.')

# Call the main function if the file is being run as
# a standalone program.
if '__name__'  == '__main__': 
    main()
            

        

