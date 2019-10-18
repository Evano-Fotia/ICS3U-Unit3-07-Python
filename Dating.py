#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program sees if the person is old enough to date the grandchild


def main():

    # input
    integer = int(input("Enter age: "))

    # process & output
    if integer >= 25 and integer <= 40:
        print("you can date!")
    elif integer > 40 or integer < 25:
        print("You can't date!")


if __name__ == "__main__":
    main()
