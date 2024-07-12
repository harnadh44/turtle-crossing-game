from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:

    def __init__(self):
        self.all_car = []
        self.car_sped = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_random = random.randint(-230, 230)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y_random)
            self.all_car.append(new_car)

    def mov_car(self):
        for car in self.all_car:
            car.backward(self.car_sped)

    def inc_speed(self):
        self.car_sped += MOVE_INCREMENT
