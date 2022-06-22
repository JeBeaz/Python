import random
from secrets import choice
import string

print('Lets Play Rock, Paper, Scissosrs!')

while True: 
    user_action = input('Choose (Rock, Paper, or Scissors):')
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a Tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock Smashes Scissors! You Win!")
        else:
            print("Paper Covers Rock! You Lose!")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper Covers Rock! You Win!")
        else:
            print("Scissors Cuts Paper! You Lose!")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors Cuts Paper! You Win!")
    else:
        print("Rock Smashes Scissors! You Lose!")
    
    play_again = input("Play Again? (y/n): ")
    if play_again.lower() != "y":
        break

