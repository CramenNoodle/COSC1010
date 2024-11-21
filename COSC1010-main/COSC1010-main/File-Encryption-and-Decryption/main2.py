# Carmen Grajeda 
# 11/20/11
# File Encryption and Decryption Programming Project
# Second Program
# COSC 1010 NT
#
# Constant Variables
ENCRYPTED_FILE = 'encrypted.txt' # The file that will be read and decrypted

# Local Variables
flipped_codes = {} # The Variable for the dictionary from main.py flipped
encrypted_contents = '' # The Variable for the contents of the file that is read and decrypted
decrypted_text = '' # The Variable for the decrypted text
codes = {} # The Variable for the dictionary from main.py

# This program will open the file "encrypted.txt", read the contents of the file,
# and display the decrypted contents on the screen. 

# Import the encrypted_dictionary function from main.py
from main import encrypted_dictionary

# Define a function that will grab the dictionary from main.py,
# and flip the dictionary to decrypt the contents of the file.
def decrypted_dictionary():

    # Get the dictionary from main.py
    codes = encrypted_dictionary()

    # Make a new dictionary that will flip the dictionary from main.py
    flipped_codes = {v: k for k, v in codes.items()}

    # Return the decrypted codes
    return flipped_codes

# Define a function that will open the "encrypted.txt" file,
# and display the decrypted contents on the screen.
def decrypted_contents():

    # Get the decrypted dictionary
    flipped_codes = decrypted_dictionary()

    try:
        # Open the file "encrypted.txt" and read the contents
        with open('encrypted.txt','r') as file:
            encrypted_contents = file.read()

    # use the except FileNotFoundError: to catch the error if the file is not found
    except FileNotFoundError:
        # Display an error if the file is not found
        print('The file "encrypted.txt" was not found.')
        return
    
    # use the except Exception as e: to catch any other errors
    except Exception as e:
        # Display an error if an error occurs while reading the file
        print('An error occurred while reading the file "encrypted.txt".')
        return
    
    # Decrypt the contents of the file
    decrypted_text = ''
    for char in encrypted_contents:
        if char in flipped_codes:
            decrypted_text += flipped_codes[char]
        # if the character is not in the dictionary, leave it as is
        else:
            decrypted_text += char

    # Display the decrypted contents of the file
    print(decrypted_text)

# Call the decrypted_contents function
if __name__ == '__main__':
    decrypted_contents()


    



    


    
