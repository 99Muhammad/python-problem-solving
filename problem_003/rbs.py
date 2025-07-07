from enum import Enum
import random

class RBS(Enum):
    Rock = 'r'
    Paper = 'p'
    Scissors = 's'

def get_input():
    while True:
            choice = (input("Rock, Paper, Scissors? (r/p/s): ").lower())
            if choice in ['r', 'p', 's']:
                return RBS(choice)
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

def play_round():
    while True:
            player_choice = get_input()
            computer_choice = random.choice(list(RBS))

            print(f"You chose {player_choice.name}, Computer chose {computer_choice.name}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == RBS.Rock and computer_choice == RBS.Scissors) or
                (player_choice == RBS.Paper and computer_choice == RBS.Rock) or
                (player_choice == RBS.Scissors and computer_choice == RBS.Paper)
            ):
                print("+1 for you")
            else:
                print("+1 for computer")
            
            if input("continue ? (y/n) : ").lower() == 'n':
                break
play_round()
