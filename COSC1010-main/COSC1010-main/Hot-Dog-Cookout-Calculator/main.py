#
# Carmen Grajeda
# 09/07/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 1010 NT
#
# Variable constants
hot_dog_per_package = 10
hot_dog_buns_per_package = 8
# Local Variables
numAttending = 0 # The number of people attending the cookout.
numPerPerson = 0 # The number of hot dogs and buns per person.
total = 0 # The total number of hotdog and bun packages needed. 
minHotdogs = 0 # The minimum number of hot dog packages.
minBuns = 0 # The minimum number of hot dog bun packages.
leftoverdogs = 0 # The number of leftover hot dogs from a package.
leftoverbuns = 0 # The number of leftover hot dog buns from a package.
# Get the number of people coming
numAttending= int(input('Enter the amount of people coming: '))
# Get the number of hot dogs per person.
numPerPerson = int(input('Enter the amount each person would eat: '))
# Calculate the number hot dogs per person. 
total = numAttending * numPerPerson
# Calculate the number of hot dogs needed
minHotdogs = total // hot_dog_per_package
# Calculate the number of hot dog buns needed
minBuns = total // hot_dog_buns_per_package
# Determine if the amount of people attending is large enough to need more than one package.
if leftoverdogs > 0:
    # Calculate the number of hot dogs leftover from a package if any.
    leftoverdogs = total % hot_dog_per_package
    # If there is hot dogs leftover, add additional package. 
    if leftoverdogs != 0:
        minHotdogs += 1
# Set the minimum number packages of hotdogs to one because the number of people attending is small enough to require one package. 
else:
    minHotdogs = 1
# Determine the left over hot dog, if any. 
leftoverdogs = hot_dog_per_package * minHotdogs - total
# Determine if the amount of people attending is large enough to need more than one package.
if leftoverbuns > 0:
    # Calculate the number of hot dog buns leftover from a package if any. 
    if leftoverbuns != 0:
        minBuns +=1
# Set the minimum number packages of hot dog buns to one because the number of people attending is small enough to require one package. 
else: 
    minBuns = 1
# Determine the left over hot dog buns, if any. 
leftoverbuns = hot_dog_buns_per_package * minBuns - total
# Display the number of hot dog packages needed.
print(f' Minimum number of hot dog packages needed: ', minHotdogs)
# Display the number of hot dog bun packages needed.
print(f' Minimum number of hot dog bun packages needed: ', minBuns)
# Display the number of hot dogs leftover.
print(f'Amount of hot dogs left over: ', leftoverdogs)
# Display the number of hot dog buns leftover.
print(f'Amount of hot dog buns leftover: ', leftoverbuns)


    


 

