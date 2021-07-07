from random import choice
from sys import exit

def game_start():
    world_list = ['hola','mundo','adios']
    guesses = 0
    game_over = False
    answer = choice(world_list)
    word_length = len(answer)
    guessed = []
    current_guess = ''

    print("Welcome to \"Gues The Word\"")
    print("The goal of the game is to guess the secret word by guessing letters one at a time.")
    print(f"The word is {word_length} letters long")

    while game_over == False:
        print_puzzle(answer, guessed)
        current_guess = input("Please enter a letter, or press 'Enter' to solve: ")
        guesses += 1
        if current_guess == '':
            if solve(answer):
                win(guesses)
        elif current_guess in guessed:
            print('You already guessed that one!')
            guesses -= 1
        else:
            guessed.append(current_guess)




def print_puzzle(answer, guessed):
    word = ''
    for letter in answer:
        if letter in guessed:
            word += letter
        else:
            word += '*'

    print(word)
    print(f"you have already guessed: {sorted(guessed)}")



def solve(answer):
    solution_guess = input('Solve the puzzle: ')
    if solution_guess == answer:
        return True
    else:
        print('Incorrect')
        return False

def win(guesses):
    print(f'You guessed the word in only {guesses} guesses')
    play_again = input('Would you like to play again ? (y/n)')
    if play_again == 'y':
        game_start()
    elif play_again == 'n':
        print('Thanks for playing')
        exit()


game_start()

