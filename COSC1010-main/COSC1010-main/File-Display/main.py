#
# Carmen Grajeda
# 10/9/2024
# File Display Programming Project
# COSC 1010 NT
#

# This program opens a file named numbers.txt 
# and displays all of the numbers in the file.

# Open the file. 
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Close the file.
myfile.close()
    
                  

     
