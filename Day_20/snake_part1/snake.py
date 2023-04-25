from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def start_game(self):
        snake = []
        till = 0
        for x in range(0, 3):
            snake.append(Turtle())
            snake[x].penup()
            snake[x].shape("square")
            snake[x].color("white")
            snake[x].goto(till, 0)
            till -= 20
        return snake

    def __init__(self):
        self.snake = self.start_game()
        self.position = 0

    def turn_snake(self, num):
        if self.position != num:
            next = 90
            if self.position > num:
                next = -90
            while self.position != num:
                self.snake[0].left(next)
                self.position += next

    def left(self):
        self.turn_snake(LEFT)

    def right(self):
        self.turn_snake(RIGHT)

    def up(self):
        self.turn_snake(UP)

    def down(self):
        self.turn_snake(DOWN)

    def Move(self):
        for index in range(2, 0, -1):
            new_y = self.snake[index - 1].ycor()
            new_x = self.snake[index - 1].xcor()
            self.snake[index].goto(new_x, new_y)
        self.snake[0].forward(20)
        #self.snake[0].left(90);