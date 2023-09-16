from turtle import Turtle
from random import randint, choice

DIRECTION = [(143, 233), (-36, 36)]
PLAYER = [0, 1]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.ball_direction()
        self.penup()

    def ball_direction(self):
        player = choice(PLAYER)
        self.setheading(randint(DIRECTION[player][0], DIRECTION[player][1]))

    def bounce(self):
        self.setheading(self.heading()*(-1))

    def bounce_x(self):
        current_heading = self.heading()
        new_heading = (360-current_heading) + 180
        self.setheading(new_heading)

    def respawn(self):
        self.goto((0, 0))
        self.ball_direction()
