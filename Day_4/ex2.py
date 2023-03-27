# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
many = len(names)
i = int(random.randint(0, many - 1))
print(names[i] + " is going to buy the meal today!")
