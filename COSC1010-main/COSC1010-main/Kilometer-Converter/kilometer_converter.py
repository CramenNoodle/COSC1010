#
# Carmen Grajeda
# 09/17/2024
# Kilometer Converter Programming Project
# COSC 1010 NT

# This program converts kilometers to miles.
# Global Constant 
conversion_factor = 0.6214
# Local variables 
kilometers = 0.0 # The kilometers the user imputs
miles = 0.0 # Results of the converted kilometers to miles. 
show_miles = 0.0 # The distance in kilometers converted into miles
# The main function gets a distance in kilometers and calls 
# the show_miles function to convert it.
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter the distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from 
# kilometers to miles and displays the result.
def show_miles(km):
    # Calculate the miles.
    miles = km * conversion_factor

    # Display the miles.
    print(f'{km:.2f} kilometers equals {miles:.2f} miles.')

# Call the main function.
main()

