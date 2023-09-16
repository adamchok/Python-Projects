import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.start()
        scoreboard.increase_score()
        if scoreboard.score % 3 == 0:
            scoreboard.increase_level()
            car_manager.increase_speed()
        if scoreboard.level % 4 == 0:
            car_manager.increase_cars(scoreboard.level)

screen.exitonclick()
