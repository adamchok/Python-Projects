from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.chances = [1]

    def create_car(self):
        random_chance = randint(1, 6)
        for chance in self.chances:
            if random_chance == chance:
                car = Turtle()
                car.penup()
                car.color(choice(COLORS))
                car.shape("square")
                car.shapesize(stretch_len=2, stretch_wid=1)
                car.goto(x=300, y=randint(-250, 250))
                car.setheading(180)
                self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def increase_cars(self, level):
        numbers = [2, 3, 4, 5, 6]
        if level == 4:
            self.chances.append(numbers[0])
        elif level == 8:
            self.chances.append(numbers[1])
        elif level == 12:
            self.chances.append(numbers[2])
        elif level == 16:
            self.chances.append(numbers[3])
        elif level == 20:
            self.chances.append(numbers[4])
