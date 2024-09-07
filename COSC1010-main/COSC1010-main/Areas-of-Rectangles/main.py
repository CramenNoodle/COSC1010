#
# Carmen Grajeda
# 09/07/2024
# Areas of Rectangles Programming Project
# COSC 1010 NT
#
# Local variables
area_1 = 'length_A,'' width_A'
area_2 = 'lenght_B,''width_B'
# Get length A
length_A = int(input('Enter the length of retangle 1:'))
# Get width A
width_A = int(input('Enter the width of retangle 1:'))
# Get length B
length_B = int(input('Enter the length of retangle 2:'))
# Get width B
width_B = int(input('Enter the width of rectangle 2:'))
# Calculate area A
area_1 = length_A * width_A
# Calculate area B
area_2 = length_B * width_B
# Print area comparison using if-elif-else statements
if area_1 > area_2:
    print('Rectangle one has a greater area.')
elif area_2 > area_1:
    print('Rectangle two has a greater area.')
else:
    print('Both rectangles have the same area.')

