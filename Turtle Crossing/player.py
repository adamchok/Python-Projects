from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_finish_line()
        self.penup()
        self.shape("turtle")
        self.start()

    def draw_finish_line(self):
        self.penup()
        self.hideturtle()
        self.goto(x=300, y=FINISH_LINE_Y)
        self.pendown()
        self.setheading(180)
        self.forward(600)
        self.showturtle()

    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
