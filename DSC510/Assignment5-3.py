# BSA 510
# Week 4
# BlackBoard Post 5.3: Understanding
# Author: Michael Hotaling
# 06/30/2020

import time


def prime_check(number):
    if number == 2:
        return " is prime"
    elif number == 1 or number % 2 == 0 or number < 0:
        return " is not prime"
    else:
        for i in range(3, number):
            if number % i == 0:
                return " is not prime"
        return " is prime"


def prime_check2(number):
    if number == 2:
        return " is prime"
    elif number == 1 or number % 2 == 0 or number < 0:
        return " is not prime"
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                return " is not prime"
        return " is prime"


def prime_check3(number):
    if number == 2:
        return " is prime"
    elif number == 1 or number % 2 == 0 or number < 0:
        return " is not prime"
    else:
        for i in range(3, int(number/2)+1, 2):
            if number % i == 0:
                return " is not prime"
        return " is prime"


def prime_check4(number):
    if number == 2:
        return " is prime"
    elif number == 1 or number % 2 == 0 or number < 0:
        return " is not prime"
    else:
        for i in range(3, int((number ** 0.5) + 1), 2):
            if number % i == 0:
                return " is not prime"
        return " is prime"


def count_primes(number):
    primes = [2]
    x = 3
    if number < 2:
        return 0
    while x <= number:
        for y in range(3, x):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return primes


def count_primes2(number):
    primes = [2]
    x = 3
    if number < 2:
        return 0
    while x <= number:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return primes


def count_primes3(number):
    primes = [2]
    x = 3
    if number < 2:
        return 0
    while x <= number:
        for y in range(3, int(x ** 0.5) + 1, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return primes


def count_primes4(number):
    primes = [2]
    x = 3
    if number < 2:
        return 0
    while x <= number:
        for y in primes[0:int((len(primes) ** (1/2.17636) + 1))]:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return primes


if __name__ == "__main__":
    while True:
        user_entry = int(input("Please enter the number you wish to check: "))
        print()
        start = time.time()
        check1 = prime_check(user_entry)
        print(str(user_entry) + check1)
        end = time.time()
        print("prime_check took " + str(end - start) + " to run")

        start = time.time()
        check2 = prime_check2(user_entry)
        end = time.time()
        print("prime_check2 took " + str(end - start) + " to run")

        start = time.time()
        check3 = prime_check3(user_entry)
        end = time.time()
        print("prime_check3 took " + str(end - start) + " to run")

        start = time.time()
        check4 = prime_check4(user_entry)
        end = time.time()
        print("prime_check4 took " + str(end - start) + " to run")

        print(check1 == check2 == check3 == check4)