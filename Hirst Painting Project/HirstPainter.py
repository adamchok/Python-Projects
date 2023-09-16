# import colorgram
import turtle
from random import randint


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


def hirst_painting(row, column, dot_size, gap_size):
    """
    Create the painting

    Parameters: Row, column, dot size, and gap size
    """

    turtle.colormode(255)
    turtle.screensize(10000, 10000)

    # rgb_colors = []
    # colors = colorgram.extract('image.jpg', 30)
    # for color in colors:
    #     rgb_colors.append(color.rgb)

    painter = turtle.Turtle()
    painter.shape("circle")
    painter.shapesize(0.01)
    painter.speed("fastest")
    painter.penup()

    def get_into_position(half_length, half_width):
        painter.backward(half_length)
        painter.right(90)
        painter.forward(half_width)
        painter.left(90)

    def paint_row():
        for _ in range(column):
            painter.pendown()
            painter.dot(dot_size, random_colour())
            painter.penup()
            painter.forward(gap_size)

    def next_row(total_length):
        painter.left(90)
        painter.forward(gap_size)
        painter.left(90)
        painter.forward(total_length)
        painter.left(180)

    length = column * gap_size
    width = row * gap_size
    get_into_position(length / 2, width / 2)
    for _ in range(row):
        paint_row()
        next_row(length)
    painter.color("white")

    screen = turtle.Screen()
    screen.exitonclick()


print("Welcome to Hirst Paintings!")
while True:
    try:
        no_row = int(input("How many rows would you like?: "))
        no_column = int(input("How many columns would you like?: "))
        size_of_gap = int(input("What gap size would you like?: "))
        size_of_dot = int(input("Pick a dot size (5 to 15): "))
        hirst_painting(no_row, no_column, size_of_dot, size_of_gap)
        break
    except ValueError:
        print("Invalid value. Please try again by inputting integer values (for all).")
