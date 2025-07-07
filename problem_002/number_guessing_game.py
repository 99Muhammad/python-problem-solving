import random

def get_input():
    return input('Guess a number between 1 and 100: ')

def number_guessing_game():
    random_number = random.randint(1, 100)

    while True:
        user_input = get_input()

        if user_input.isdigit():
            guess = int(user_input)

            if guess < random_number:
                print('Too low!')
            elif guess > random_number:
                print('Too high!')
            else:
                print(' Congratulations! You guessed the number!')
                break
        else:
            print('Please enter a valid number.')

number_guessing_game()
