# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Michael Hotaling
# 07/06/2020


# I made several math functions in week 4 so I thought I might use them for this homework assignment :)


def mean(numbers):
    # This one is pretty easy. We can just create a variable named summer and set it equal to 0.
    # For every element in the list, we can add the value to the summer and once we reach the end of the list
    # we can divide the summer by the number of elements.
    summer = 0
    for i in numbers:
        summer += i
    average = (summer / len(numbers))
    return average


def median(numbers):
    # Added this for fun
    # This function will find the median value in a list
    # We will first sort the list from lowest to highest and find the length of the list
    # If the list length is even, we will need to use floor division to find the two middle values and average them
    # If the list is odd, we just need to pull the middle value
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        med1 = numbers[length // 2]
        med2 = numbers[length // 2 - 1]
        med = (med1 + med2) / 2
        return med
    else:
        med = numbers[(length // 2)]
        return med


def variance(numbers):
    # Variance can be understood as a measurement of the spread between numbers in an array of numbers
    # Simplified, variance can be though of as how far each value in a set is from the mean of the set and,
    # therefore, from every other number in the set.
    # We can create a new list and fill it with the calculated values. Once that's done, we can take the mean
    var_list = []
    mu = mean(numbers)
    for i in numbers:
        var_list.append((i - mu) ** 2)
    return mean(var_list)


def square_root(number):
    # https://www.cse.wustl.edu/~cytron/101Pages/f08/Notes/SquareRoot/sqrt.html
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    # https://en.wikipedia.org/wiki/Newton%27s_method
    # This one was actually pretty tricky. We could just use the built in exponential function ** and use 0.5 as the
    # exponent, but that wouldn't be any fun. Instead, we can create a recursive function to approximate the square
    # root of a number. This is known as Newtons Method
    start = 0
    end = number
    guess = 0
    threshold = 0.0000000000001

    while end - start > threshold:
        guess = (start + end) / 2
        m_square = guess * guess
        if abs(m_square - number) <= threshold:
            return guess
        elif m_square < number:
            start = guess
        else:
            end = guess
    return guess


def standard_deviation(numbers):
    # Now that we have defined square root and variance, all we need to do here is use both to find the square root.
    return square_root(variance(numbers))


def temp_recorder(temp):
    # This function records the entries from the user by appending an empty list.
    # The escape argument, also known as the sentinel value, will be the string "quit"
    # There is error handling just in case the user inputs an invalid data type like a string or boolean
    while True:
        # This while loop will continuously ask for inputs until the user inputs "quit"
        # quit can be in any format since we check to see if the lower case values are equal to the sentinel string
        user_input = input("Please input temperature number " + str(len(temp) + 1) + ": ")
        if user_input.lower() == "quit":
            return temp
        # This is error handling just in case the user tries to input an invalid data type. Since this is a while
        # loop, the user has the opportunity to try and input another value without the program crashing
        try:
            temp.append(float(user_input))
        except ValueError:
            print("Invalid entry: Please try again!")

    # Here we will print out the results of the list.
    # If the list is empty, or something else went wrong, it will print the except statement.


def pretty_format(temp_list):
    try:
        print()
        print("The list of temperatures is [" + ', '.join(map(str, temp_list)) + "]")
        print("The maximum temperature is " + str(max(temp_list)))
        print("The minimum temperature is " + str(min(temp_list)))
        print("The number of measurement inputs is " + str(len(temp_list)))
        print("The average value of measurement inputs is " + str(mean(temp_list)))
        print("The median value of the measurement inputs is " + str(median(temp_list)))
        print("The variance of the measurement inputs is " + str(variance(temp_list)))
        print("The standard deviation of the measurement inputs is " + str(standard_deviation(temp_list)))
    except ValueError:
        print("Something went wrong!")
        print("Did you forget to input a temperature? ")
        print("Please try again!")


def main():
    # We will greet the user and print the instructions on how to use the program
    temps = []
    print()
    print("Welcome to the temperature recorder!")
    print("Input a numeric value below.")
    print("Type 'quit' to exit the program")
    # We will use a while loop to ask the user if they want to run the program again
    # We also added a neat little feature by asking the user if they want to continue where they left off
    # That way, they don't have to worry about accidentally inputting the sentinel value and losing their data
    while True:
        print()
        temps = temp_recorder(temps)
        pretty_format(temps)
        print()
        again = input("Would you like to run the program again? [y/n]:  ")
        if again.lower() != "y":
            break
        # Here, we give the user the opportunity to either continue with their list, or start fresh.
        user_continue = input("Would you like to continue where you left off? [y/n]: ")
        if user_continue.lower() != "y":
            # This line resets the temp values
            temps = []
            print("List erased! Starting over!")
    print("Goodbye!")
    exit()


# Here, we will call the program with the __main__ statement.
if __name__ == "__main__":
    main()
