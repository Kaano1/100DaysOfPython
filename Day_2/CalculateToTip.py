#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float( input("Welcome to the tip calculate\nWhat was the total bill?\n") )
percentage = float( input("What percentage tip would you like to give? 10, 12 or 15\n") )
people = int( input("How many people to split the bill?\n") )

calculate = round((bill / people) * ((percentage + 100) / 100), 2)
print("Each person should pay " + str(calculate))
