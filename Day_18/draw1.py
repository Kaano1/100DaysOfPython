from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("classic")
for _ in range(4):
    timmy.forward(50)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
