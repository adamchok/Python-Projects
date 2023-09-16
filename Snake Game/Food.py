from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # creating 10 by 10 circle: #
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x=x, y=y)

