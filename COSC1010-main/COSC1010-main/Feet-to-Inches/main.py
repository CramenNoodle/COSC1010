#
# Carmen Grajeda
# Date
# Feet to Inches Programming Project
# COSC 2409 DNT

# This program converts 12 inches into feet with the users input. 
# Global Constant 
INCHES_PER_FOOT = 12 # Constant for the number of inches per foot. 
# Local Variables 
feet = 0 # Parameter variable
feet_to_inches = 'feet' # The function that accepts a number of feet as an argument that accepts a number of feet as an argument.
# the main function
def main():
    # Get the number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert the number given by user to inches 
    print(feet,'equals',feet_to_inches(feet),'inches.') # Displays the number of inches in that many feet

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT # The value of the argument 

# Call the main function.
main()

