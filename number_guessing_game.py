#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program is a game where the user tries to guess the correct number


import constants


def main():
    # This function tells the user if their guess is correct

    # Input
    guessed_number = int(input("Guess what my number between 0 and 10 is: "))
    print("")

    # Process & Output
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed it!")
    if guessed_number != constants.CORRECT_NUMBER:
        print("Wrong number!")
    print("\nDone.")


if __name__ == "__main__":
    main()
