from art import logo
from art import vs
from game_data import data
from os import system
from random import randint

def game(next, score):
	first = randint(0, len(data))

	while next:
		system("clear")
		print(logo)
		if (score != 0):
			print(f"You're right! Current score: {score}.")
		second = -1
		while (second == -1 or first == second):
			second = randint(0, len(data))
		print("Compare A: " + data[first]["name"] + ", a " + data[first]["description"] + ", from " + data[first]["country"] + ".")
		print(vs)
		print("Compare B: " + data[second]["name"] + ", a " + data[second]["description"] + ", from " + data[second]["country"] + ".")
		section = input("Who has more followers? Type 'A' or 'B': ").upper()
		if (section == 'A' and data[first]["follower_count"] > data[second]["follower_count"]):
			score += 1
		elif (section == 'B' and data[second]["follower_count"] > data[first]["follower_count"]):
			first = second
			score += 1
		else:
			next = False
	return (score)

score = game(True, 0)

system("clear")
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
system("rm -rf __pycache__/")