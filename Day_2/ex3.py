# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_age = int(age)
days =  (365 * 90) - number_age * 365
weaks = (52 * 90) - number_age * 52
month = (12 * 90) - number_age * 12 

print(f"You have {days} days, {weaks} weeks, and {month} months left.")