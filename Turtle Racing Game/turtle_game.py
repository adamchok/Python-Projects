from turtle import Turtle, Screen
from random import randint

# turtle_1 = Turtle(shape="turtle")
# turtle_2 = Turtle(shape="turtle")
# turtle_3 = Turtle(shape="turtle")
# turtle_4 = Turtle(shape="turtle")
# turtle_5 = Turtle(shape="turtle")
# turtle_6 = Turtle(shape="turtle")
#
# turtles = {
#     turtle_1: {"color": "red", "position": -125},
#     turtle_2: {"color": "orange", "position": -75},
#     turtle_3: {"color": "yellow", "position": -25},
#     turtle_4: {"color": "green", "position": 25},
#     turtle_5: {"color": "blue", "position": 75},
#     turtle_6: {"color": "purple", "position": 125},
# }

game_start = False
error = True

screen = Screen()
screen.setup(width=500, height=400)

position = [-125, -75, -25, 25, 75, 125]
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
user_bet = ""

while error:
    user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color (red, "
                                                             "orange, yellow, green, blue, purple: ").lower()
    if user_bet in color:
        game_start = True
        error = False
    else:
        print("Invalid input. Please try again.")

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    all_turtle.append(turtle)
    turtle.penup()
    turtle.color(color[i])
    turtle.goto(x=-240, y=position[i])

while game_start:
    for turtle in all_turtle:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"Winner: {winner.title()} turtle\nYou won!")
            else:
                print(f"Winner: {winner.title()} turtle\nYou lost.")
            game_start = False

screen.exitonclick()
