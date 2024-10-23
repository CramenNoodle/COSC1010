#
# Carmen Grajeda
# 10/22/2024
# Lottery Number Generator Programming Project
# COSC 1010 NT

# Constant Variable
NUM_AMOUNT = 7 # The Variable for the max amount of numbers.
START = 0 # Start of the random number range.
END = 9 # End of the random number range.

# Local Variables 
numbers = [0] * 7

# This program displays 7 random 
# numbers in the range of 0 through 9.

# Import random module
import random

# define the main function
def main():
    # Create a list and initialize the value of num_amount
    numbers = [0] * NUM_AMOUNT
        
    # Generate a list with 7 random numbers in the range of 0 through 9.
    for index in range(NUM_AMOUNT):
        # Assign numbers sub index and generate a random number
        numbers[index] = random.randint(START, END)
    
    # Display the random numbers
    print('Here are your lottery ticket numbers: ')
    print(numbers)
    
# Call the main function
main()





    





