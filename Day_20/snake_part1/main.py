from turtle import Turtle, Screen
from snake import Snake
import time

snake = Snake()
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()

screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

turn_on = True
while turn_on:
    screen.update()
    time.sleep(0.1)

    snake.Move()

screen.exitonclick()