#
# Carmen Grajeda
# 11/13/2024
# Capital Quiz Programming Project
# COSC 1010 NT

# Local variables 
capitals = {} # The variable for the dictionary of states and capitals.
correct = 0 # The variable for the number of correct answers.
incorrect = 0 # The variable for the number of incorrect answers.
state = '' # The variable for the state.
answer = '' # The variable for the user's input
continue_playing = '' # The variable for the user's input to continue playing or not.

# This program tests the user on the names of the captials by the state they input,
# lets the user know if they are correct or incorrect and 
# continue until the user quits.  

# Import the random module.
import random

# Define the main function. 
def main():
    # Initialize the dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Initialize the variables to keep count of number of correct and incorrect answers.
    correct = 0
    incorrect = 0

    # Quiz the user until they quit
    while True:
        # Randomly pick a state from the dictionary
        state = random.choice(list(capitals.keys()))

        # Ask the user to enter an answer
        answer = input(f'What is the capital of {state}? ')

        # Check to see if the user is correct or incorrect
        if answer.lower() == capitals[state].lower():
            # Add 1 to the correct count
            correct += 1
            # Display that the answer is correct
            print('Correct!')
        else:
            # Add 1 to the incorrect count
            incorrect += 1
            # Display that the answer is incorrect
            print(f'Incorrect. The correct answer is {capitals[state]}.')
    
        # Display the amount of correct responses
        print('Correct responses:', correct)
        # Display the amount of incorrect responses
        print('Incorrect responses:', incorrect)

        # Ask the user if they want to keep playing 
        continue_playing = input('Do you want to continue playing? (Enter "y" to continue, "n" to  quit): ')
        # If the user wants to continue playing, continue the loop
        if continue_playing.lower() != 'y':
            # exit the loop
            break
    
    # Display a message to the user
    print('Thank you for playing!')

# Call the main function.
if __name__ == '__main__':
    main()
    






