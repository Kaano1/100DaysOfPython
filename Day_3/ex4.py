# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

wallet = 0

if (size == "L"):
    wallet += 25
elif (size == "M"):
    wallet += 20
elif (size == "S"):
    wallet += 15

if add_pepperoni == "Y":
    if (size == "S"):
        wallet += 2
    else:
        wallet += 3

if (extra_cheese == "Y"):
    wallet += 1

print(f"Your final bill is: ${wallet}.")