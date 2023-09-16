from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def right_tilt():
    tim.setheading(tim.heading() - 10)


def left_tilt():
    tim.setheading(tim.heading()+10)


def reset():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=right_tilt)
screen.onkeypress(key="a", fun=left_tilt)
screen.onkeypress(key="c", fun=reset)

screen.exitonclick()
