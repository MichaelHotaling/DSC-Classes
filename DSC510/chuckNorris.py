# DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Michael Hotaling
# 07/29/2020


import requests
import time
import webbrowser


def chuck_norris_joke(category):
    try:
        # I need an if statement to pull the correct base url if the user wants a specific category
        if category == "random":
            api_response = requests.get('http://api.chucknorris.io/jokes/random', verify=False)
        else:
            api_response = requests.get('http://api.chucknorris.io/jokes/random?category=' + category, verify=False)
        json_response = api_response.json()
        return json_response.get('value')

        # Raise an error if the API rejects the query
    except requests.HTTPError:
        print("An HTTP Error has occurred. Please try again later.")
        exit()


def category_puller():
    # This pulls the categories from the API. We only need to pull this once.
    categories = requests.get('http://api.chucknorris.io/jokes/categories', verify=False).json()
    return categories


def joke_selector(categories):
    # This function returns the category of joke the user wants to select.
    # I am literally terrible at using dictionaries, so I decided to use two different lists instead.
    # This is terrible.
    category_numbers = 1
    category_number_list = []
    print("Here are the categories: \nYou can enter either the category name or number: ")
    print("-" * 49)
    for category in list(categories):
        print(" {0:>2} - {1}{2}".format(category_numbers, category.upper()[0], category[1::]))
        category_number_list.append(str(category_numbers))
        category_numbers += 1

    # Random is also a category, but it isn't listed in the API list. So let's just add it.
    # This was previously running each time the list was pulled, so I set it up to check whether or not random is
    # already in the list
    if 'random' not in categories:
        print(" {0:>2} - {1}".format(category_numbers, "Random"))
        categories.append("random")
        category_number_list.append(str(category_numbers))
    print("-" * 49)
    # print(categories)
    # print(category_number_list)

    # Now we can ask the user what kind of joke they want. If they input the type of category, we will just return it.
    # If they input a numerical value, we can index the list.
    # If it's not in either, we will return "Invalid request"
    while True:
        joke_selection = input("What kind of joke would you like to hear?: ").lower()
        if joke_selection in categories:
            return joke_selection
        elif joke_selection in category_number_list:
            return categories[int(joke_selection)-1]
        else:
            print("Invalid request: Please try again!")


def create_output(joke_list):
    # This is a function I made to export the jokes. Pretty much entirely lifted from last weeks assignment
    file_name = "Chuck_Norris_Jokes.txt"
    output = open(file_name, "w")
    output.write("Chuck Norris Jokes\n")
    output.write("-" * len("Chuck Norris Jokes") + "\n")
    joke_number = 1
    for joke in joke_list:
        output.write("{:>3}) {}\n".format(joke_number, joke))
        joke_number += 1
    output.close()
    webbrowser.open(file_name)


def main():
    # The main function is a bit long
    # Greeting
    print("Welcome to the Chuck Norris Joke Machine")
    # Pull the categories
    categories = category_puller()
    x = 1
    z = 0
    joke_list = []
    while True:
        category = joke_selector(categories)
        while True:
            try:
                y = int(input("How many jokes would you like to hear?: "))
                if y <= 0:
                    print("Please input a positive integer value")
                    continue
                elif y > 999:
                    print("That's too many jokes! \nPlease pick a smaller number!")
                    continue
                z = z + y
                break
                print("Please input a positive integer value")
            except ValueError as error:
                print(str(error) + " :Please enter a positive integer!")

        # This whole block should be it's own function, but I'm finding it hard to return the joke list for output
        print_line = "Pulling {0} {1} joke(s):"
        print("-" * len(print_line.format(y, category)))
        print(print_line.format(y, category))
        print("-" * len(print_line.format(y, category)))
        while x <= z:
            joke = chuck_norris_joke(category)
            print("{:>3}) {}".format(x, joke))
            joke_list.append(joke)
            x += 1
            time.sleep(2)
        print("-" * 40)

        while True:
            user_continue_request = input("Would you like to see more jokes? [y/n]: ").lower()
            if user_continue_request == "y":
                break
            elif user_continue_request == "n":
                if input("Would you like to export your jokes to txt? [y/n]: ").lower() == "y":
                    create_output(joke_list)
                print("Goodbye!")
                exit()
            else:
                print("Invalid request")


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()  # I need this line to run the program on my computer. Very annoying
    main()
