#Write your code below this line 👇
import math

def paint_calc(h, w, c):
    calculate = math.ceil( (h * w) / c )
    print(f"You'll need {calculate} cans of paint")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(h=test_h, w=test_w, c=coverage)

