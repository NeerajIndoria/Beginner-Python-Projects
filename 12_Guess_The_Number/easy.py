#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guesss againt actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear
clear()
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    guesses = 10  
else:
    guesses = 5

number = random.randint(100)
flag = True
while flag:
    if guesses == 0:
       print("You've run out of guesses, you lose.")
    else:
        print(f"You have {guesses} attempts remaining to guess the number.")
    user_input = int(input("Make a guess: "))
    if user_input > number :
        print("Too high.\nGuess again.")
        guesses -= 1
    elif user_input < number:
        print("Too low.\nGuess again.")
        guesses -= 1
    else:
        print(f"You got it! The answer was {number}.")
        flag = False