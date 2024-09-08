#
# Carmen Grajeda
# 09/07/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 1010 NT
#
# variable constants
hot_dog_per_package = 10
hot_dog_buns_per_package = 8
# Get the number of people coming
people = int(input('Enter the amount of people coming:'))
hotdog_per_person = int(input("Enter the amount each person would eat:"))
# Calculate the number hot dogs per person 
total_needed_hotdogs = people * hotdog_per_person
# Calculate the number of hot dogs needed
needed_hotdogs = total_needed_hotdogs // hot_dog_per_package
# Calculate the number of hot dog buns needed
needed_hotdog_buns = total_needed_hotdogs // hot_dog_buns_per_package
# Calculate the left over hot dogs 
leftover_dogs = total_needed_hotdogs % hot_dog_per_package
# Calculate the left over hot dog buns
leftover_buns = total_needed_hotdogs % hot_dog_buns_per_package
# Display the amount needed
print(f"You will need {needed_hotdogs} hot dogs.")
print(f"You will need {needed_hotdog_buns} hot dog buns.")
# Display the amount leftover using if statement
if leftover_dogs != 0:
    print(f'You will have {leftover_dogs} hot dogs leftover.')
if leftover_buns != 0:
    print(f'You will have {leftover_buns} hot dog buns leftover.')
else:
    print('Yay no left overs to clean up!')
    


 

