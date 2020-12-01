# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Michael Hotaling
# 06/25/2020


def regular_price():
    # We can declare the standard price here so we can call it later when checking how much money the user saved
    # This can be helpful if the standard price ever changes or if we need to raise prices in the future
    return 0.87


def price_calculation(feet):
    # Price Calculation. This function checks to see if the user is eligible for a bulk discount
    # We have three different discounts, > 500ft, >250ft and >100ft
    # We've added abs() in the function just in case the user needs to return some cable
    if abs(feet) > 500:
        return 0.50
    elif abs(feet) > 250:
        return 0.70
    elif abs(feet) > 100:
        return 0.80
    else:
        return regular_price()


def bill(feet, price):
    # Bill calculator. This function multiplies the amount of feet by the price of the cable per foot to get the
    # total price
    price = feet * price
    return price


def input_cable_length():
    # Create the function to ask the user for how many feet of fiber they need
    # There is error handling, so if the user inputs an incorrect value, the function will loop
    try:
        length = float(input('How many feet of fiber optic cable is required?: '))
        return length
    except ValueError:
        print("Oops! Please put in a numerical value. eg. 55, 3.14, 9999")
        print("Please try again!")
        return input_cable_length()


def print_receipt(company_name, cable_length, cable_price, final_cost):
    # Printing the receipt
    # This program will intake 4 variables, the company name, the cable length, the cable price, and the final cost
    print("--" + company_name + " Cable Company--")
    print("--Fiber Optic Receipt--")
    print("--Feet of Cable: " + str(cable_length) + "--")
    print("--Price per Foot: " + (f'${cable_price:,.2f}'.replace('$-', '-$')) + "--")
    print("--Total Cost: " + (f'${final_cost:,.2f}'.replace('$-', '-$')) + "--")
    if cable_price != 0.87 and cable_length > 0:
        print("--You saved " + (f'${cable_length * regular_price() - final_cost :,.2f}'.replace('$-', '-$')) +
              " with our discount!--")
    print("--Please come again soon!--")


def main():
    # Introduction
    print('Hello! Welcome to the Fiber Optic Price Calculator!')

    # Asking the user which company they are from
    company = input('Which company are you from?: ')
    print("Okay! You are from " + company + ". That's great to hear!")

    # Use the input_cable_length() function to ask the user how many feet of cable they need
    # We will then call all the functions we need to calculate their bill
    fiber_length = input_cable_length()
    fiber_price = price_calculation(fiber_length)
    total_cost = bill(fiber_length, fiber_price)

    # This is just a fun little message to let the user know they are getting our bargain pricing
    if fiber_price != 0.87 and fiber_length > 0:
        print("Good news! You're eligible for our bulk discount!")

    # Here are some statements if the user inputs negative values or a 0
    if fiber_length < 0:
        print('Oh! Okay! You need to return ' + str(-fiber_length) + ' feet of fiber cable. We will credit you ' +
              f'${-total_cost:,.2f}'.replace('$-', '-$'))
    elif fiber_length == 0:
        print("Don't need any cable today? That's okay! We are always open! ")
    else:
        print('You will need ' + str(fiber_length) + " feet of fiber optic cable! That will cost you " +
              f'${total_cost:,.2f}'.replace('$-', '-$'))
    # Some print statements to create some room between the chat and the receipt
    print()

    # Calling the print function
    print_receipt(company, fiber_length, fiber_price, total_cost)


if __name__ == "__main__":
    main()
