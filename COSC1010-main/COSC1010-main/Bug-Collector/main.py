#
# Carmen Grajeda        
# 09/09/2024
# Bug Collector Programming Project
# COSC 1010 NT
#
# Initialize variables for bugs and total number of bugs collected.
total_bugs = 0
# Get number of bugs collected each day using a for loop.
for day in range (1, 6):
    print('Enter the amount of bugs you collected on day', day)
    bugs = int(input())
    total_bugs += bugs      
# Display the total number of bugs collected.
print('The total amount of bugs collected is', total_bugs, 'bugs.')

