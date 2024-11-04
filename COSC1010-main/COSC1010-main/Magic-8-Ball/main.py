#
# Carmen Grajeda
# 10/23/2024
# Magic 8 Ball Programming Project
# COSC 1010 NT


# Constant Variables 
RESPONSE_FILE = '8_ball_responses.txt' # The file used to import the responses.

# Local Variables
again = 'y' # Variable to control the loop. 
response_list = [] # Variable for the list of responses.

# This program simulates a Magic 8 Ball that will generate a response
# to a yes or no question.

# Import random module
import random

# Define the main function
def main():
    # Open the file '8_ball_responses' for reading.
        RESPONSE_FILE = open('8_ball_responses.txt', 'r')
        try:
            # Read the contents of the file into a list.
            response_list = RESPONSE_FILE.readlines()
        
        # Close the file
        finally:
             RESPONSE_FILE.close()

        # Strip the \n from each element
        for index in range(len(response_list)):
            response_list[index] = response_list[index].rstrip('\n')

        # Create a variable to control the loop.
        again = 'y' 

        # Use the while again loop to ask a question and generate a response from the user. 
        while again == 'y' or again == 'Y':
            # Prompt the user to ask a question
            userQuestion = input('Ask the Magic 8 Ball a Question: ')

            # Display a random response from the response list.
            print(response_list[random.randint(0, len(response_list) - 1)])

            # Ask the user if they want to ask another question
            print('Do you want to ask another question? ')
            # Get y or no from the user to continue or end 
            again = input('y = yes, anything else = no: ')
            print()

# Call the main function
main()











