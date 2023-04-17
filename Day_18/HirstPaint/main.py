from turtle import Turtle, Screen, colormode
import random
import colorgram


tim = Turtle()
tim.penup()
colormode(255)
tim.speed("fastest")


def get_rgb(rgb):
    randColor = (rgb.r, rgb.g, rgb.b)
    return randColor


tmp_color = colorgram.extract("image.jpg", 20)
color = []
for send in tmp_color:
    color.append(get_rgb(send.rgb))

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
