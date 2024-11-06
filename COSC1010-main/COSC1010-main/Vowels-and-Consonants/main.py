#
# Carmen Grajeda
# 11/5/2024
# Vowels and Consonants Programming Project
# COSC 1010 NT
#

# Local Variables
num_vowels = 0 # The variable for the number of vowels in the string
num_consonants = 0 # The variable for the number of consonants in the string
user_string = '' # The variable for the string from the user input
vowels = ['a','e','i','o','u'] # The list of vowels
c_count = 0 # Variable to initializes an ccumulator consonants
v_count = 0 # Variable to initializes an accumulator for vowels

# This program accepts a string from a users input
# as an argument and returns the number of vowels and consonants,
# and displays the number of vowels and consonants it contains.

# Define the main function
def main():
    # Get a string from the user.
    user_string = input('Enter a string of characters: ')

    # Report the vowels and constants in the string. 
    print('That string has', num_vowels(user_string), 'vowels and', \
          num_consonants(user_string), 'consonants.')
    
# The num_vowels function returns the number of 
# vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a','e','i','o','u']

    # Initialize an accumulator.
    v_count = 0

    # Count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count.
    return v_count

# The num_consonants function returns the number of 
# consonants in the string passed as an argument.
def num_consonants(s):
    # Make a list containing the vowels.
    vowels = ['a','e','i','o','u']

    # Initialize an accumulator.
    c_count = 0

    # Count the consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # Return the consonant count.
    return c_count

# Call the main function.
main()
