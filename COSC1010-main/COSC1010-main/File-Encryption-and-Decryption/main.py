#
# Carmen Grajeda
# 11/20/11
# File Encryption and Decryption Programming Project
# COSC 1010 NT
#

# Constant Variables
INFILE = 'text.txt' # The file that will be read and encrypted
OUTFILE = 'encrypted.txt' # The file that will be written to with the encrypted text

# Local Variables 
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{}|;:,.<>?/`~ ' # The characters that will be encrypted
codes = '%9@#!$^&*()-_=+1234567890qwertyuioasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' # The codes that will be assigned to the characters
codes_dictionary = {} # The dictionary that will map characters to their intended codes
contents = '' # The Variable for the contents of the file that is read
encrypted_text = '' # The Variable for the encrypted text

# This program will open the file text.txt, read the contents of the file, 
# and use the dictionary to write an encrypted verson of the file's 
# contents to the encrypted.txt file. 

# The encrypted_dictionary function will return a dictionary that will assign
# "codes" to each letter of the alphabet." 
def encrypted_dictionary():
    # Characters that will be encrypted
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{}|;:,.<>?/`~ '
    # codes that will be assigned to the characters
    codes = '%9@#!$^&*()-_=+1234567890qwertyuioasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

    # Create a dictionary that will map characters to their corresponding codes.
    codes_dictionary = {characters[i]: codes[i] for i in range(min(len(characters), len(codes)))}
    # return
    return codes_dictionary

# The encrypt function will open a file called text.txt, read the contents of the file,
# and use the dictionary to write an encrypted verson of the file's contents
# to the encrypted.txt file.
def encrypt():

    # Create a dictionary 
    codes = encrypted_dictionary()

    # Open the file text.txt and read the contents of the file
    with open(INFILE,'r') as file:
        contents = file.read()

    # Encrypt the contents of the file 
    encrypted_text = ''
    for char in contents:
        if char in codes:
            encrypted_text += codes[char]
        else:
            encrypted_text += char

    # Write the encrypted verson of the file's contents to the output file
    with open(OUTFILE, 'w') as file:
        file.write(encrypted_text)

# Call the encrypt function
if __name__ == '__main__':
    encrypt()







    



    


    
