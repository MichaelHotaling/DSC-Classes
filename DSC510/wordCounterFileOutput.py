# DSC 510
# Week 8
# Programming Assignment Week 8
# Author: Michael Hotaling
# 07/21/2020

import string
import os  # To print out the directory of the file
import webbrowser  # to open the file once it is created


def add_words(words, word_dictionary):
    # We can use an iterative function to add each word to the library
    # If the word doesn't yet exist in the library, we can set the value equal to 1
    for word in words:
        if word != "":
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1


def process_line(line, word_dictionary):
    # We will first call strip to remove the leading and trailing spaces in the string
    line = line.strip()
    # Next, we convert all the characters to lower case.
    line = line.lower()
    # This ia bit more complicated. We need to remove special characters from our input.
    # We can use translate to covert the special characters to spaces
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Finally, we can split all the words in each line using spaces as the delimiter
    words = line.split()
    # We can then call the process_add_words function to add the words to the dictionary
    add_words(words, word_dictionary)


def process_file(word_dictionary, output_filename, title=""):
    output = open(output_filename, "w")
    output.write("{:^35}\n".format(title + ": " + str(len(word_dictionary)) + " unique words"))
    output.write("{:-^35}\n".format("-"))
    output.write("| {:>5} | {:<15}|{:>7} |\n".format("Index", "Word", "Count"))
    output.write("{:-^35}\n".format("-"))
    index = 1
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        output.write("| {:>5} | {:<15}|{:>7} |\n".format(index, key, word_dictionary[key]))
        index += 1
    output.write("{:-^35}\n".format("-"))


def csv_process_file(word_dictionary, output_filename, title=""):
    output = open(output_filename, "w")
    # output.write("Length of the dictionary: " + str(len(word_dictionary) + "\n"))
    output.write("{:^35}\n".format(title + ": " + str(len(word_dictionary)) + " unique words"))
    output.write("{},{},{}\n".format("Index", "Word", "Count"))
    index = 1
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        output.write("{},{},{}\n".format(index, key, word_dictionary[key]))
        index += 1


def main():
    path = os.getcwd()
    file = "gettysburg.txt"
    # file = input("What is the file name?: ")

    try:
        gba_file = open(file, 'r')
    except FileNotFoundError as error:
        print(error)
        print("Please make sure the file is in the correct directory before running.")
        exit()

    output_filename = input("txt and csv formats are recommended\nEnter the output file name: ")
    if os.path.exists(output_filename):
        if input("There is already a file with that name. \nWould you like to overwrite? [y/n]: ").lower() != "y":
            exit()
    word_dictionary = dict()
    for line in gba_file:
        process_line(line, word_dictionary)
    gba_file.close()
    format_finder = output_filename.split(".")
    format_finder = format_finder[len(format_finder)-1]

    # This block could probably be optimized
    if format_finder == "csv":
        # Special condition for CSV formats
        # The will use the special function to export the file with comma separation
        print("Exporting File as {0}".format(format_finder.upper()))
        csv_process_file(word_dictionary, output_filename, title=file)
    elif "." in output_filename:
        print("Exporting File as {0}".format(format_finder.upper()))
        process_file(word_dictionary, output_filename, title=file)
    else:
        print("No File Format Selected. Defaulting to TXT")
        output_filename = output_filename+".txt"
        process_file(word_dictionary, output_filename, title=file)

    print("{0} Exported to {1}".format(output_filename, path))
    if input("Would you like to open the file now? [y/n]: ").lower() == "y":
        print("Opening File...")
        webbrowser.open(output_filename)
    if input("Would you like to delete the file now? [y/n]: ").lower() == "y":
        print("Deleting File...")
        os.remove(output_filename)
        print("File Deleted")


if __name__ == "__main__":
    main()
