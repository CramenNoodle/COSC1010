#
# Carmen Grajeda
# 09/019/2024
# Budget Analysis Programming Project
# COSC 1010 NT
#
# This program calculates the users monthly budget and expenses 
# and if the user is over or under budget.

# Constant variables
budget = int(input('Enter the budget of the month: '))
another = 'y' #Variable to control the loop.
# Local Variables
expenses = 0.0

#Declare the accumulator
total = 0.0

# Process one or more expenses
while another == 'y' or another == 'Y':
    # Get the expenses
    expenses = float(input('Enter the expenses: '))
    # Validate the expenses
    while expenses < 0:
        print('ERROR: the expenses cannot be negative.')
        expenses = float(input('Enter the correct ' +
                               'expense amount: '))
    #Calculate the total expenses.
    total += expenses
    # Do this again?
    another = input('Do you have another expense? ' +
                    '(Enter y for yes): ')

# Display if the users total amount over or under budget.
if total > budget:
    print(f'You are over your budget by $', format(abs(total),',.2f'))
elif total == budget:
    print(f'Your budget is enough for expenses!')
else:
    print(f'You are under the budget by $',format(abs(total),',.2f'))
# Display the total 
print(f'Total: ${total:,.2f}')






 

