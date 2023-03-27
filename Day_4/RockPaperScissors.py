# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = [rock, paper, scissors]
user_i = int( input() )
comp_i = random.randint(0, 2)

print(choose[user_i] + "\n\n" + choose[comp_i])

if (user_i == 0 and comp_i != 1) or (user_i == 1 and comp_i != 2) or (user_i == 2 and comp_i != 0):
    print("You Win")
else:
    print("You lose")