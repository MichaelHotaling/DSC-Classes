# DSC 510
# Week 5
# Programming Assignment Week 5
# Author: Michael Hotaling
# 07/02/2020

# One thing I'd like to bring up is that according to PEP8,
# Function names should be lowercase, with words separated by underscores as necessary to improve readability.


def performCalculation(operator):
    """
    This function takes in an operator value and will perform a numeric
    operation with two number inputs. We can handle errors by checking if the operator
    is valid by checking if it's in the list below
    hello
     """

    if operator not in ['+', '-', '*', 'x', 'X', '/']:
        print('Unknown operator. Please try again.')
        return
    # Request two numbers from the user to perform the operation on
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid data type. Please try again.")
        return

    # Addition operation
    if operator == "+":
        print('Sum is: ' + str(a + b))
    # Subtraction operation
    elif operator == "-":
        print('Difference is: ' + str(a - b))
    # Multiplication operation
    # I threw in a couple more possible operator values for multiplication
    # since x and X are common
    elif operator == "*" or operator == "x" or operator == "X":
        print('Product is: ' + str(a * b))
    # Division operation
    else:
        # If the second input is a 0, throw an error
        if b == 0:
            print('Quotient is: undefined')
            return
        print('Quotient is: ' + str(a / b))


def calculateAverage():
    """
    As per the instructions, this function intakes no arguments
    We start the average calculation by creating a local variable called summer as to not override the sum() function
    We will set summer equal to 0
    Average is equal to the total sum of the inputs divided by the number of inputs
    so we will add all the inputs to this value then call the division once the
    summation is completed
    """
    summer = 0
    try:
        # Some error handling just in case the input is invalid
        number_of_numbers = int(input("How many numbers to you wish to average?: "))
    except ValueError:
        print("Invalid data type. Please try again")
        return
    if number_of_numbers <= 0:
        # More error handling in case the number of numbers is less than 1
        print("Whoops! That's not allowed! Please try again!")
        return
        # Create a recursive function to add values to the sum variable
    for i in range(1, number_of_numbers + 1):
        try:
            summer += float(input("What is number " + str(i) + "?: "))
        except ValueError:
            print("Invalid data type. Please try again")
            return
        # Divide the total
    summer /= number_of_numbers
    print("The average of those numbers is: " + str(summer))


def main():
    # A warm introduction
    print("Hello. Welcome to the calculator app!")
    print()
    # Create a while loop to keep the program running until the user requests to exit
    # Asking the user what they want to do
    while True:
        print("Which program would you like to run?")
        print("Enter 1 for numerical operations")
        print("Enter 2 to calculate an average")
        print("Enter 3 to exit the program")

        request = input("What would you like to do?: ")

        # Error handling if the inputs aren't valid
        if request not in ["1", "2", "3"]:
            print("Oops! That's an invalid request. Please try again!")
            print()
        # Operation request
        elif request == '1':
            performCalculation(input("Valid inputs are:\n Addition: + \n Subtraction: -\n Multiplication: * or x\n "
                                     "Division: /\n Please enter an operator sign: "))
            print()
        # Average request
        elif request == '2':
            calculateAverage()
            print()
        # Exit request
        else:
            print("Goodbye!")
            exit()


if __name__ == '__main__':
    main()
