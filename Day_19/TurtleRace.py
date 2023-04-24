from turtle import Turtle, Screen
from random import randint

color = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_game():
    turtleList = [Turtle("turtle"), Turtle("turtle"), Turtle("turtle"), Turtle("turtle"), Turtle("turtle"), Turtle("turtle")]
    y = -100
    for index in range(0, 6):
        turtleList[index].color(color[index])
        turtleList[index].penup()
        turtleList[index].goto(-230, y)
        turtleList[index].pendown()
        y += 40
    return turtleList


def start_game(TrutleList, guess):
    index = 0
    while index != 6:
        TrutleList[index].forward(randint(10, 20))
        if index == 5:
            index = 0
        else:
            index += 1
        if TrutleList[index].xcor() > 230:
            print(color[index] + " Turtle winner!")
            break
    if guess == color[index]:
        print("You're right man!!!")
    else:
        print("Unfortunately you aren't good bet")



screen = Screen()
screen.setup(500, 400)
guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

list = create_game()
start_game(list, guess)

screen.exitonclick()
