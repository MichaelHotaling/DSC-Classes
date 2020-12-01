# DSC 510
# Week 10
# Programming Assignment 10.1
# Author: Michael Hotaling
# 08/03/2020


import datetime
import sys
import webbrowser
from money import Money
import os


class CashRegister(object):
    def __init__(self):
        self.thing = []
        self.number = []
        self.price = []
        self.total_price = []
        self.amount = 0
        self.sales_tax = 0.0825

    def add_item(self, item, quantity, value):
        # For each item input by the user, the class will append the corresponding list with information.
        # Ideally, this should be simplified to a dictionary or tuple, but I am short on time this week
        self.thing.append(item)
        self.number.append(quantity)
        self.price.append(value)
        self.total_price.append(round(quantity * value, 2))

    def sales_tax(self):
        # This just returns the sales tax
        return self.sales_tax

    def payment(self, payment_amount):
        # This will calculate the full payment required for the transaction
        self.amount = payment_amount - (sum(self.total_price) * (1 + self.sales_tax))
        return self.amount

    def printout(self):
        # This will print out the receipt for the transaction using the class variables.
        print("=" * 44)
        print("|{:^42}|".format("Receipt"))
        print("|{:^42}|".format(datetime.datetime.now().strftime("%m/%d/%Y")))
        print("|{:^42}|".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
        print("=" * 44)
        print("| {0:<40} |  \n| {2:<10} | {1:>11} | {3:>12}  |".format("Item", "Quantity", "Price/Item", "Price"))
        print("=" * 44)
        for i in range(0, len(self.thing)):
            print("| {0:<40} |  \n| {2:<10} | {1:>11} | {3:>13} |"
                  .format(self.thing[i],
                          self.number[i],
                          Money(self.price[i], "USD").format("en_US"),
                          Money(self.total_price[i], "USD").format("en_US")))
        print("=" * 44)
        print("| {1:<20}{5:>20} |\n"
              "| {2:<20}{6:>20} |\n"
              "| {3:<20}{7:>20} |\n"
              "| {4:<20}{8:>20} |"
              .format(sum(self.number),
                      "Number of Items: ",
                      "Subtotal: ",
                      "Sales Tax: ",
                      "Total Price: ",
                      int(round(sum(self.number), 0)),
                      Money(sum(self.total_price), "USD").format('en_US'),
                      Money((sum(self.total_price) * self.sales_tax), "USD").format('en_US'),
                      Money(sum(self.total_price) * (1 + self.sales_tax), "USD").format('en_US')))

    def append_logs(self):
        # I wanted this to be able to record the transactions so the business could then model their metrics
        # Ideally, the program should export to a table format, but I was having issues with the CSV export
        # Also, it'd be a good idea to create an inventory system to know how many items we have on hand.
        with open("log_book.txt", "a+") as log_book:
            if os.stat("log_book.txt").st_size == 0:
                log_book.write("-" * 71 + "\n")
                log_book.write("| {:<20} | {:>12} | {:>12} | {:>14} |\n".format("Date", "Net Income", "Sales Tax",
                                                                                "Total Payment"))
                log_book.write("-" * 71 + "\n")
            log_book.write("| {:<20} | {:>12} | {:>12} | {:>14} |\n".format(
                datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                Money(sum(self.total_price), "USD").format('en_US'),
                Money((sum(self.total_price) * self.sales_tax), "USD").format('en_US'),
                Money(sum(self.total_price) * (1 + self.sales_tax), "USD").format('en_US')))


def main():
    print("Welcome to the Cash Register App")
    print("Please input the item name, followed by the quantity and price per item")
    print()
    while True:
        register = CashRegister()
        while True:
            item = input("Item Name: ")
            while True:
                try:
                    quantity = float(
                        input("Quantity: "))  # Changed this to float since some things are measured by weight
                    break
                except ValueError:
                    print("Invalid Entry")
            while True:
                try:
                    value = float(input("Value of Item: $"))
                    break
                except ValueError:
                    print("Invalid Entry")
            register.add_item(item, quantity, value)
            keep_going = input("Continue? [y/n]: ").lower()
            if keep_going == "n":
                print()
                register.printout()

                # To avoid redundant code, I'm going to use that trick I discovered in Week 8 to save outputs of the
                # receipts
                default = sys.stdout
                if not os.path.isdir("receipts"):
                    os.mkdir("receipts")
                receipt_name = "receipts\\{}.txt".format(datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
                receipt_printout = open(receipt_name, "w")
                sys.stdout = default
                while True:
                    try:
                        payment_amount = float(input("| Payment Amount:                   $"))
                        break
                    except ValueError:
                        pass

                # TODO This should be part of the class function, but I'm short on time this week since I'm so busy
                #  at work.
                print("| {0:<20}{1:>20} |".format("Change:",
                                                  Money(register.payment(payment_amount), "USD").format('en_US')))
                print("=" * 44)
                sys.stdout = receipt_printout
                register.printout()
                print("| {0:<20}{1:>20} |".format("Payment Amount:",
                                                  Money(payment_amount, "USD").format('en_US')))
                print("| {0:<20}{1:>20} |".format("Change:",
                                                  Money(register.payment(payment_amount), "USD").format('en_US')))
                print("=" * 44)
                sys.stdout = default
                receipt_printout.close()
                webbrowser.open(receipt_name)
                register.append_logs()
                break
        print()
        while True:
            user_continue = input("More Transactions? [y/n]: ")
            if user_continue.lower() == "n":
                print("Thanks for using the Cash Register App!")
                exit()
            elif user_continue.lower() == 'y':
                break
            else:
                print("Invalid Entry")


if __name__ == "__main__":
    main()
