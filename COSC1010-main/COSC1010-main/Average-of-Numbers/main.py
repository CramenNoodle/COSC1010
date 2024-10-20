#
# Carmen Grajeda
# 10/16/2024
# Average of Numbers Programming Project
# COSC 1010 NT

# Constant Variables
infile = 'numbers.txt' # The variable that stores the file
# local variables
total = 0.0 # variable that ititilizes the accumulator
count = 0 # variable that controls the count 
value = 0.0 # variable that converts numbers into floats
average = 0 # variable that keeps the average of the numbers

# This program calculates the averages in the file numbers.txt

# Define the main function
def main():
    # Initilize an accumulator
    total = 0.0
    # Variable to control the count
    count = 0

    # Open the numbers.txt file
    infile = open('numbers.txt','r')

    # Get the values from the file and total them
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
# Call the main function
main()





        










        








