
# Carmen Grajeda
# 10/22/2024
# Exception Handling Programming Project
# COSC 1010 NT 

# This program adjusts the "Average of numbers" assignment and handles any "IOError" that are raised when
# open and read, as well any "ValueError" from the file when converted to a number. 

# Constant Variables
infile = 'numbers.txt' # The variable that stores the file 

# Local Variables
total = 0.0 # Variable that initilizes the accumulator
count = 0 # Variable that controls the count
value = 0.0 # Variable that converts numbers into floats
average = 0 # Variable that keeps the average of the numbers

# Define the main function
def main():
    # Initilize an accumulator
    total = 0.0

    # Use the try/except statement with three except clauses
    try:
        # Open the numbers.txt file
        infile = open('numbers.txt','r')

        # Variable to control the count.
        count = 0

        # Get the values from the file and total them.
        for line in infile:
            # Convert line to a float
            value = float(line)
            # Add 1 to the count variable.
            count += 1 
            # Add the value to the total
            total += value

        # Close the file
        infile.close()

        # Calculate the average of the numbers 
        average = total / count 

        # Display the average
        print(f'The average of all the numbers in "numbers.txt" is: {average: .2f}.')
    # except statement to handle "IOError" that are raised when the file is opened
    # and data is read from it. 
    except IOError:
        print('An error occurred trying to read the file.')
    
    # Except statement to handle "ValueError" that are raised when the items that are read in the file 
    # are converted to a number.
    except ValueError:
        print('Non-numeric data found in the file.')
    # Except statement for any other error that is not handled by the other except clauses. 

    except:
        print('An Error occured.')
        
# Call the main function
main()