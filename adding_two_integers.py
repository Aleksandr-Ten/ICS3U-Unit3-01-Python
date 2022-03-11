#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program calculates addition between two integers
# with user input


def main():
    # this function calculates total from first and second numbers

    # input
    first_number = float(input("Enter the first number to add (integer): "))
    second_number = float(input("Enter the second number to add (integer): "))

    # process
    total = first_number + second_number

    # output
    print("")
    print("{0:,.0f} + {1:,.0f} = {2:,.0f}".format(first_number, second_number, total))
    print("\nDone")


if __name__ == "__main__":
    main()
