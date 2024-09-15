#
# Carmen Grajeda        
# 09/09/2024
# Bug Collector Programming Project
# COSC 1010 NT

# Constant Variable to represent the amount of days. 
day = 5
# Local variables 
numBugs = 0
# Initilized variable for bugs and total number of bugs collects.
total = 0 
# Get the bugs collected for each day using a for loop.
for day in range (1, 6):
    print('Enter the amount of bugs you collected on day', day)
    # Calculate the number of bugs collected each day. 
    numBugs = int(input()) 
    # Add number of bugs to the accumulator.
    total += numBugs      
# Display the total number of bugs collected.
print('The total amount of bugs collected is: ', total, 'bugs.')

