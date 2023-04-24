from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_w():
    turtle.forward(10)


def move_s():
    turtle.backward(10)


def move_turn_right():
    turtle.right(5)


def move_turn_left():
    turtle.left(5)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkeyrelease(key="w", fun=move_w)
screen.onkeyrelease(key="s", fun=move_s)
screen.onkeyrelease(key="a", fun=move_turn_left)
screen.onkeyrelease(key="d", fun=move_turn_right)
screen.onkeyrelease(key="c", fun=clear_screen)

screen.exitonclick()
