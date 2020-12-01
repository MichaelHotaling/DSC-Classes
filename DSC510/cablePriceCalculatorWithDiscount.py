# DSC 510
# Week 3
# Programming Assignment Week 3
# Author: Michael Hotaling
# 06/15/2020


# Introduction
print('Hello! Welcome to the Fiber Optic Price Calculator!')

# Asking the user which company they are from
# Convert the company name to a string in case it is something like "101" Cable Company
company = input('Which company are you from?: ')
print("Okay! You are from " + str(company) + ". That's great to hear!")

# Asking the user how many feet of cable they will need for their job
# Check to see if the amount is the correct data type. If not, it will abort the program
try:
    fiberLength = float(input('How many feet of fiber optic cable is required?: '))
except ValueError:
    print("Oops! Please put in a numerical value!")
    exit()

# We will check for the price per length of cable here
# If the user requests more than a certain amount of cable, they will get a discount
if fiberLength > 500:
    fiberPrice = 0.50
elif fiberLength > 250:
    fiberPrice = 0.70
elif fiberLength > 100:
    fiberPrice = 0.80
else:
    fiberPrice = 0.87

if fiberPrice != 0.87:
    print("Good news! You're eligible for our bulk discount!")

# We will need to round the total price to prevent float issues
print('You will need ' + str(fiberLength) + " feet of fiber optic cable! That will cost you " +
      (f'${fiberPrice * fiberLength:,.2f}'.replace('$-', '-$')))

# Some print statements to create some room between the chat and the receipt
print()

# Printing the receipt
print("--" + company + " Cable Company--")
print("--Fiber Optic Receipt--")
print("--Feet of Cable: " + str(fiberLength) + "--")
print("--Price per Foot: " + (f'${fiberPrice:,.2f}'.replace('$-', '-$')) + "--")
print("--Total Cost: " + (f'${fiberPrice * fiberLength:,.2f}'.replace('$-', '-$')) + "--")

if fiberPrice != 0.87:
    print("--You saved " + (f'${fiberLength * 0.87 - fiberPrice * fiberLength :,.2f}'.replace('$-', '-$')) +
          " with our discount!--")

print("--Please come again soon!--")
