from turtle import Turtle, Screen
import time
from Score import Score
from Paddle import Paddle
from Ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Pong!")
screen.tracer(0)

centre_line = Turtle()
centre_line.color("white")
centre_line.hideturtle()
centre_line.penup()
centre_line.goto(x=0, y=280)
centre_line.setheading(270)
centre_line.shape("square")
centre_line.width(5)
for _ in range(19):
    centre_line.pendown()
    centre_line.forward(10)
    centre_line.penup()
    centre_line.forward(20)

score_1 = Score((-100, 250))
score_2 = Score((100, 250))

paddle = Paddle()
ball = Ball()

screen.update()

screen.listen()
screen.onkeypress(key="w", fun=paddle.go_up_1)
screen.onkeypress(key="s", fun=paddle.go_down_1)
screen.onkeypress(key="Up", fun=paddle.go_up_2)
screen.onkeypress(key="Down", fun=paddle.go_down_2)

while True:
    screen.update()
    time.sleep(0.04)
    # ball.forward(10)

    if score_1.score == 5:
        score_1.game_over("Player 1")
        break
    elif score_2.score == 5:
        score_2.game_over("Player 2")
        break

    if (paddle.player_1.distance(ball) < 50 and ball.xcor() < -350) or (paddle.player_2.distance(ball) < 50 and ball.xcor() > 350):
        ball.bounce_x()

    if ball.xcor() < -370:
        score_2.increase_score()
        ball.respawn()
        paddle.respawn()
        time.sleep(1)

    elif ball.xcor() > 370:
        score_1.increase_score()
        ball.respawn()
        paddle.respawn()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
