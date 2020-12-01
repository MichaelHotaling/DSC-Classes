# Mike's Stupid Number Machine


def num_to_word(i):
    # I added the teen numbers to the singles list. This is useful for numbers between 1-19, but if we ever want to 
    # increase range of this program, we will run into issues. ie 116. 
    singles_and_teens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                         "twelve",
                         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", ""]

    # Second digit lists
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # We don't need a hundred list technically. We should be able to check the length of the number. If it is 3, 
    # we can pull The first digit, index the singles list, and add "hundred" to the string. The rest is self 
    # explanatory. 

    # Futuristic
    hundreds_and_beyond = ["", "", "hundred", "thousand", "thousand", " hundred thousand", "million"]

    if i <= 19:
        print(singles_and_teens[i])
    elif 20 <= i <= 99:
        print(str(tens[int(str(i)[0]) - 2]) + " " + str(singles_and_teens[int(str(i)[1])]))
    elif len(str(i)) == 3 and str(i)[1:] == "00":
        print(str(singles_and_teens[int(str(i)[0])]) + " hundred")
    elif len(str(i)) == 3 and str(i)[1] == "0" or str(i)[1] == "1":
        print(str(singles_and_teens[int(str(i)[0])]) + " hundred and " + str(singles_and_teens[int(str(i)[1:])]))
    else:
        print(str(singles_and_teens[int(str(i)[0])]) + " hundred and " + str(tens[int(str(i)[1]) - 2]) + " " + str(
            singles_and_teens[int(str(i)[2])]))


while True:
    try:
        num_to_word(int(input("Enter a number between 1 and 999: ")))
    except:
        print("Invalid Input")
