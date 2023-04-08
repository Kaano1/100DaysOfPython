from art import logo
from os import system
import random

randNum = random.randint(1, 100)

def guessing(attempts):
    find = False
    while (not find):
         print(f"You have {attempts} remaining to guess the number")
         guess = int( input("Make a guess: ") )
         if (guess == randNum):
             print(f"You got it! The answer was {guess}")
             find = True
         elif (attempts <= 1):
             find = True
             print("You lost!")
         elif (guess > randNum):
             print("too high")
         else:
             print("too low")
         attempts -= 1
        
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm think of a number between 1 to 100.")
section = input("Choose a difficulty. Type 'easy' or 'hard': ")

if (section == "easy"):
    guessing(10)
elif (section == "hard"):
    guessing(5)
else:
    system("clear")

system("rm -rf __pycache__/")