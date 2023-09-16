from turtle import Turtle


FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.level = 1
        self.goto(-170, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level} Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over.", align="center", font=FONT)
