"""
The computer generates the number chosen by the user.
"""

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c) ?\n")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'h' and feedback != 'l' and feedback != 'c':
            print("Sorry. I don't understand. Give me the right feedback.\n")
    print(f"Yes! The computer has guessed your number {guess} correctly.")

computer_guess(50)
