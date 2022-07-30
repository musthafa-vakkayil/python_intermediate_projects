from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,10)

        if random_chance == 1:
            timmy = Turtle("square")
            timmy.color(COLORS[random.randint(0,5)])
            timmy.penup()
            timmy.turtlesize(stretch_len=2, stretch_wid=1)
            timmy.goto(300, random.randint(-260, 260))
            timmy.setheading(180)
            self.cars.append(timmy)

    def move_car(self):
        for i in self.cars:
            i.forward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT

