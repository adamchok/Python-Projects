from turtle import Turtle


PADDLE_POS = [(-360, 0), (360, 0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        for position in PADDLE_POS:
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.penup()
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.goto(position)
            self.paddles.append(paddle)
        self.player_1 = self.paddles[0]
        self.player_2 = self.paddles[1]

    def respawn(self):
        self.player_1.goto(PADDLE_POS[0])
        self.player_2.goto(PADDLE_POS[1])

    def go_up_1(self):
        current_y = self.player_1.ycor()
        self.player_1.goto(x=-360, y=current_y + 15)

    def go_down_1(self):
        current_y = self.player_1.ycor()
        self.player_1.goto(x=-360, y=current_y - 15)

    def go_up_2(self):
        current_y = self.player_2.ycor()
        self.player_2.goto(x=360, y=current_y + 15)

    def go_down_2(self):
        current_y = self.player_2.ycor()
        self.player_2.goto(x=360, y=current_y - 15)

