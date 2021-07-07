# Guess the number
from random import randrange

low_number = 1
high_number = 10
tries = 0
guess = None # empty value
answer = randrange(low_number, high_number + 1)

print("Welcome to \"Guess  the number\"")
print("The goal of the game is to guess what number I'm thinking of in the fewest guesses possible")
print("Let's get started")

while guess != answer:
    guess = input(f"Guess a number between {low_number} and {high_number} ")
    tries += 1
    if int(guess) < answer:
        print('That number is too low! Try again...')
    elif int(guess) > answer:
        print("That number is too high! Try again...")
    elif int(guess) == answer:
        print("That's right! You win! ")
        print(f"It only took you {tries} tries")
        break

print("Thank you for playing!")






