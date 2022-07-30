import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
board = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_car()

    if player.ycor() > 280:
        board.update_level()
        player.restart()
        cars.level_up()

    for car in cars.cars:
        if player.distance(car) < 20:
            board.game_over()
            game_is_on = False

screen.exitonclick()
