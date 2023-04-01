#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

length_answer = 0

#Check guessed letter
while (length_answer != word_length):
	guess = input("Guess a letter: ").lower()
	for position in range(word_length):
		letter = chosen_word[position]
		if letter == guess:
			length_answer += 1
			display[position] = letter
	print(display)
if (length_answer == word_length):
	print("You win")