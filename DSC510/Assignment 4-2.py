# DSC 510
# Week 4
# BlackBoard Post 4.2: Interests
# Author: Michael Hotaling
# 06/28/2020


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


def covariance(numbers_x, numbers_y, p=False):
    # Covariance calculates the relationship between two sets of numbers. There are two methods to calculate
    # covarience. One is using the population statistics and one is using a sample size. Since sample sizes are more
    # more common, I added an argument and set the default value to being False. If the population is true, the user
    # can add another argument "p = True"
    mean_x = mean(numbers_x)
    mean_y = mean(numbers_y)
    lst_x = []
    lst_y = []
    lst_xy = []
    for i in numbers_x:
        lst_x.append(i - mean_x)
    for j in numbers_y:
        lst_y.append(j - mean_y)
    for k in range(0, len(numbers_x)):
        lst_xy.append(lst_x[k] * lst_y[k])
    if p:
        cov = sum(lst_xy) / (len(numbers_x))
    else:
        cov = sum(lst_xy) / (len(numbers_x) - 1)
    return cov


def correlation(numbers_x, numbers_y):
    # Population Correlation Coefficient
    corr = covariance(numbers_x, numbers_y, p=True) / (standard_deviation(numbers_x) * standard_deviation(numbers_y))
    return corr


def pearson_correlation(numbers_x, numbers_y):
    # Pearson Correlation Coefficient
    n = len(numbers_x)
    lst_xy = []
    lst_xx = []
    lst_yy = []
    for i in range(0, len(numbers_x)):
        lst_xy.append(numbers_x[i] * numbers_y[i])
    for j in numbers_x:
        lst_xx.append(j * j)
    for k in numbers_y:
        lst_yy.append(k * k)
    sum_x = sum(numbers_x)
    sum_y = sum(numbers_y)
    sum_xx = sum(lst_xx)
    sum_yy = sum(lst_yy)
    sum_xy = sum(lst_xy)
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = (((n * sum_xx) - (sum_x * sum_x)) * ((n * sum_yy) - (sum_y * sum_y))) ** 0.5
    pearson = numerator / denominator
    return pearson


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


def factorial(number):
    intnumber = number
    if intnumber != int(number):
        raise TypeError("Factorial calculations require integer values")
    elif number == 0:
        return 1
    elif number > 0:
        x = 1
        while number != 1:
            x *= number
            number -= 1
        return int(x)
    else:
        number = abs(number)
        x = 1
        while number != 1:
            x *= number
            number -= 1
        return int(-x)


if __name__ == "__main__":
    # I used data from
    # https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/#Pearson
    # to verify that the calculations were correct
    # x = [1692, 1978, 1884, 2151, 2519]
    # y = [68, 102, 110, 112, 154]
    lst = [1, 5, 7, 22, 94, -59, 0, 2, 5, 7, 88, 49, 51]
    x = [43, 21, 25, 42, 57, 59]
    y = [99, 65, 79, 75, 87, 81]
    number = 8
    print("The mean is " + str(mean(lst)))
    print("The median is " + str(median(lst)))
    print("The variance is " + str(variance(lst)))
    print("The standard deviation is " + str(standard_deviation(lst)))
    print(str(number) + "! is " + str(factorial(float(number))))
    print("sqrt of " + str(number) + " is " + str(square_root(number)))
    print("sqrt of " + str(number) + " using ** 0.5 is " + str(number ** 0.5))
    print("The difference between them is " + str(square_root(number) - number ** 0.5))
    print("Sample covarience is " + str(covariance(x, y)))
    print("Population covariance is " + str(covariance(x, y, p=True)))
    print("Correlation is " + str(correlation(x, y)))
    print("Pearson is " + str(pearson_correlation(x, y)))
    print(x)
    print(y)
