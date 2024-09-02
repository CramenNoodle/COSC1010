#
# Carmen Grajeda
# 09/01/2024
# Sales Prediction Programming Project
# COSC 2409 DNT


# Variables to hold the sales total and the profit
annualprofitpercentage = 0.23
# Get the amount of projected sales.
projectedAmount = float(input("Enter the projected sales:"))
# Calculate the projected profit.
profit = projectedAmount * annualprofitpercentage
# Display the profit.
print('The profit is $', format(profit,',.2f'))
# Print the projected profit.
