#
# Carmen Grajeda        
# 09/09/2024
# Bug Collector Programming Project
# COSC 1010 NT

# Constant Variable
num_bugs = 0 # The number of bugs collected each day. 
# Initilized variable for bugs and total number of bugs collects.
total = 0 
# Determine the amount of bugs collected each day using a for loop.
for day in range (1, 6):
    print('Enter the amount of bugs you collected on day', day)
    # Calculate the number of bugs collected each day. 
    num_bugs = int(input()) 
    total += num_bugs      
# Display the total number of bugs collected.
print('The total amount of bugs collected is: ', total, 'bugs.')

