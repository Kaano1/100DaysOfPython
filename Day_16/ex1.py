from turtle import Turtle
from turtle import Screen

timmy = Turtle()
print(timmy)
print("position man positionnn: " + str(timmy.position()))
timmy.shape("turtle")
timmy.color("red", "blue")
timmy.forward(100)
print("position man positionnn: " + str(timmy.position()))

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

