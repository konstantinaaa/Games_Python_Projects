"""
The user tries to guess the number chosen by the computer.
"""



import random

def guess(x):
    random_number = random.randint(1, x) # return a number between 1 - x (both included)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a numbers between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Congrats! You have guessed the number {random_number} correctly.")


guess(10)

