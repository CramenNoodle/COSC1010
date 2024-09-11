#
# Carmen Grajeda
# 09/019/2024
# Budget Analysis Programming Project
# COSC 1010 NT
#
# This program calculates the users monthly budget.
# Constant Variables.
budget = 0.0
expenses = 0.0
keep_going = 'y' # Variable to control the loop.
# Initilize an accumlator variable.
total = 0.0
#Get the monthly budget.
budget = int(input('Enter your budget for this month:'))
# Process one or more items.
while keep_going == 'y' or  keep_going == 'Y':
    # Get the monthly expenses
    expenses = float(input('Enter your monthly expenses:'))
    total += expenses
    # Do this all over again.
    keep_going = input('Do you have any other expenses? ' + 
                       'Enter y for yes:')
# Display the results with the if-elif-else statment
if total > budget:
    print(f'You went ${total - budget:,.2f} over your budget.')
elif total == budget:
    print('You stayed within your budget!')
else:
    print(f'The total that you are under budget is:${total - budget:,.2f}')
# Display the total
print(f'Total: ${total:,.2f}')




