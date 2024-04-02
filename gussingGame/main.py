# Import the 'random' library for generating random numbers
import random
import time
# Import the 'pygame' library for game development and multimedia applications
import pygame
from pygame.locals import *  # Import QUIT and other constants

# Initialize the pygame library
pygame.init()


# ANSI escape codes for color
# These ANSI escape codes are used to add colored text to the console output.
# They are used for providing colorful feedback to the player during the game.

RED = '\033[91m'  # Red color
GREEN = '\033[92m'  # Green color
YELLOW = '\033[93m'  # Yellow color
END_COLOR = '\033[0m'  # Reset color

# Function to start the game
# This function handles the initial setup of the game, including level selection and game start.

def start_game():
    print("👋 Welcome to the Number Guessing Game!")

    while True:
        try:
            # Prompt the player to choose a game level (1, 2, or 3)
            level = int(input("Choose a level (1, 2, or 3): "))
            
            # Check if the chosen level is valid (1, 2, or 3)
            if level not in [1, 2, 3]:
                raise ValueError(f"{RED}❌ Invalid level. Please choose a level between 1 and 3.{END_COLOR}")
            break
        except ValueError as e:
            print(e)

    # Start the number guessing game with the chosen level
    guess_the_number(level)
"""
Function to play the number guessing game
This function is the main game logic where the player guesses the number.
It also handles different game levels and provides feedback to the player.
"""
def guess_the_number(level):
    # Calculate the maximum number based on the chosen level
    max_number = level * 10

    # Generate a random secret number between 1 and the calculated maximum
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"🎮 Welcome to Level {level} of the Number Guessing Game!")
    background_music.play()
    print(f"🤔 The system is thinking of a number between 1 and {max_number}.")

    while True:
        try:
            # Prompt the player to enter their guess
            player_guess = int(input("🤷 Enter your guess: "))
        except ValueError:
            # Handle invalid input (non-integer)
            print(f"{RED}❌ Invalid input. Please enter a valid number.{END_COLOR}")
            continue

        attempts += 1

        if player_guess < secret_number:
            print(f"{YELLOW}👇 Too low! Try again.{END_COLOR}")
            play_incorrect_sound()
        elif player_guess > secret_number:
            print(f"{YELLOW}👆 Too high! Try again.{END_COLOR}")
            play_incorrect_sound()
        else:
            play_correct_sound()
            print(f"{GREEN}🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts!{END_COLOR}")
            background_music.stop()
            break

    if level == 3:
        print(f"{GREEN}🏆 Congratulations! You have completed all levels!")
        play_correct_sound()
        display_winners_award()
        print("📲 The next version of the game will be Android-based. Stay tuned!")
        time.sleep(5)
    else:
        next_level = level + 1
        while True:
            play_next_level = input(f"Do you want to play Level {next_level}? (yes/no): ").lower()

            if play_next_level == 'yes':
                guess_the_number(next_level)
                break  # Break the loop if 'yes' is entered
            elif play_next_level == 'no':
                background_music.play()
                print("👋 Thanks for playing!")
                break  # Break the loop if 'no' is entered
            else:
                print(f"{RED}❌ Invalid choice. Please enter{END_COLOR} {GREEN}'yes' or 'no' {END_COLOR}.")

# Start the game by calling the start_game function
start_game()
