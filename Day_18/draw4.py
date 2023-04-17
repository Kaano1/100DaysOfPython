from turtle import Turtle, Screen, colormode
import random

direction = [0, 90, 180, 270]
tim = Turtle()
colormode(255)
tim.pensize(10)
tim.speed("fastest")


def draw_direction(angle):
    tim.setheading(angle)
    tim.forward(30)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    randColor = (r, g, b)
    return randColor

for _ in range(100):
    tim.color(random_color())
    draw_direction(random.choice(direction))

screen = Screen()
screen.exitonclick()
