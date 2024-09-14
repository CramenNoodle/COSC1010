#
# Carmen Grajeda
# 09/07/2024
# Areas of Rectangles Programming Project
# COSC 1010 NT
#
# Constant variables
area_1 = 'lengthA,'' widthA'
area_2 = 'lenghtB,''widthB'
# Local Variables
lengthA = 0 # Length of Rectangle 1.
widthA = 0 # Width of Rectangle 1.
lengthB = 0 # Length of Rectangle 2.
widthB = 0 # Width of Rectangle 2. 
# Get length A
lengthA = int(input('Enter the length of retangle 1:'))
# Get width A
widthA = int(input('Enter the width of retangle 1:'))
# Get length B
lengthB = int(input('Enter the length of retangle 2:'))
# Get width B
widthB = int(input('Enter the width of rectangle 2:'))
# Calculate area A
area_1 = lengthA * widthA
# Calculate area B
area_2 = lengthB * widthB
# Print area comparison using if-elif-else statements
if area_1 > area_2:
    print('Rectangle one has a greater area.')
elif area_2 > area_1:
    print('Rectangle two has a greater area.')
else:
    print('Both rectangles have the same area.')

