import turtle


START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.body = self.snakes[1:]

    def create_snake(self):
        for position in START_POSITION:
            snake = turtle.Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(position)
            self.snakes.append(snake)
        self.head = self.snakes[0]
        self.body = self.snakes[1:]

    def extend_snake(self):
        """Adding 1 more snake at the tail."""
        snake = turtle.Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        position = self.snakes[-1].position()
        snake.goto(position)
        self.snakes.append(snake)

    def move(self):
        """Moving the snake forwards."""
        for snake in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[snake - 1].xcor()
            y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(x=x, y=y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        """Moving the snake upwards."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Moving the snake upwards."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Moving the snake upwards."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Moving the snake upwards."""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def restart(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
