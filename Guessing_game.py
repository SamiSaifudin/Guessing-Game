import random
from time import sleep

def guess():
    User_guess = ""
    word = ["ROCK", "PAPER", "SCISSORS", "ELEPHANT", "YELLOW", "NAME", "BLUE", "PLATE"]
    guess_count = 0
    number_of_guesses = 7
    out_of_guesses = False
    random_index = random.randrange(len(word))

    while User_guess != word[random_index] and not(out_of_guesses):
        if guess_count < number_of_guesses:
            User_guess = input("Enter Guess: ").upper()
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("YOU ARE OUT OF GUESSES. YOU LOSE")
        sleep(2.0)
        print("THE REAL WORD WAS " + word[random_index])
    else:
        print("YOU WIN!")
        print("THE REAL WORD WAS " + word[random_index])

        sleep(2.0)


def replay():
    while True:
        Replay = input("Would you like to play again? Yes or No: ").upper()
        if Replay == "YES":
            guess()
        elif Replay == "NO":
            break
    
        
guess()
replay()