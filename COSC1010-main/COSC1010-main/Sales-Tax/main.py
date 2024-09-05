#
# Carmen Grajeda
# 09/5/2024
# Sales Tax Programming Project
# COSC 1010 NT
#

# Variable declarations
state_sales_tax = 0.05
county_sales_tax = 0.0251
purchase_amount = 150.00
# Constants for the state and county tax rates
state_tax = 0.05
county_tax = 0.025
# Get the amount of the purchase.
purchase_amount = float(input('Enter the amount of the purchase:$'))

# Calculate the state sales tax.
state_tax = purchase_amount * state_tax
# Calculate the county sales tax.
county_tax = purchase_amount * county_tax
# Calculate the total tax.
total_tax = state_tax + county_tax
# Calculate the total of the sale.
total_sale = purchase_amount + total_tax
# Print information about the sale.
print(f'The amount of the purchase is ${purchase_amount:.2f}.')
print(f'The state sales tax is ${state_tax:.2f}.')
print(f'The county sales tax is ${county_tax:.2f}.')
print(f'The total sale is ${total_sale:.2f}.')