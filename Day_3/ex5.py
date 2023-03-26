# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = "true"
love = "love"

count_t = 0
count_l = 0

i = 0

name1 = name1.lower()
name2 = name2.lower()

while (i < 4):
    count_t += name1.count(true[i]) + name2.count(true[i])
    i += 1

i = 0

while (i < 4):
    count_l += name1.count(love[i]) + name2.count(love[i])
    i += 1

ex = "."
count_t = count_t * 10 + count_l

if (count_t < 10 or count_t > 90):
    ex = ", you go together like coke and mentos."
elif (count_t >= 40 and 50 >= count_t):
    ex = ", you are alright together."


print(f"Your score is {count_t}" + ex)