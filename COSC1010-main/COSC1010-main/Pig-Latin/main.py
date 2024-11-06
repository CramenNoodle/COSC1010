#
# Carmen Grajeda
# 11/6/2024
# Pig Latin Programming Project
# COSC 1010 NT
#
# Constant Variable 
PIG_STRING = "ay"           # The constant for the string "ay"

# Local Variables
sentence = " "               # The variable for the sentence that the user will input
pig_latin = []              # The list to store the words converted to pig latin
words = sentence.split()    # The list of words split from the sentence
pig_latin_word = " "         # The variable for the word that will be converted to pig latin
pig_latin_sentence = " "     # The variable for the sentence in pig latin 

# This program reads a sentence from a users input and converts each word to "Pig Latin."

# Define a function that converts a normal sentence to Pig Latin
def convert_to_pig_latin(sentence):

    # Create an empty string to store the Pig Latin words
    pig_latin = []

    # Split the sentence into a list of words
    words = sentence.split()

    # Loop each word in the list 
    for word in words:

        # Create the Pig Latin word by moving the first letter to the end and adding "ay"
        pig_latin_word = word[1:] + word[0] + PIG_STRING

        # Append the pig latin word to the list
        pig_latin.append(pig_latin_word)

    # Concatenate the list into a single string with spaces in between
    pig_latin_sentence = ""
    for word in pig_latin:
        pig_latin_sentence += word + " "

    # Return the function using the strip method 
    return pig_latin_sentence.strip()
    

# Define the main function
def main():

    # Get the sentence from the user
    sentence = input("Enter a sentence to convert to Pig Latin: ")

    # Convert the sentence to Pig Latin
    pig_latin_sentence = convert_to_pig_latin(sentence)

    # Display the sentence converted to pig latin
    print(pig_latin_sentence)

# Call the main function
main()








