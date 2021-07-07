from random import randrange
from sys import exit

def start():
    print("Welcome to \"Guess  the number\"")
    print("The goal of the game is to guess what number I'm thinking of in the fewest guesses possible")
    print("Let's get started")
    main_loop()

def main_loop():
    low_number = 1
    high_number = 10
    tries = 0
    guess = None # empty value
    answer = randrange(low_number, high_number + 1)

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
            play_again()

def play_again():
    play_again = input("Would you like to play again? (y/n)")
    if play_again == 'y':
        main_loop()
    elif play_again == 'n':
        print("Thanks for playing!")
        exit()
    


start()


