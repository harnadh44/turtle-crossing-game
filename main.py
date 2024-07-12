from pet import Pet
from turtle import Screen
from cars import Car
import time
from level import Level

screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing capstone game")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

pet = Pet()
screen.onkeypress(pet.go_up, "Up")

car = Car()
level = Level()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.mov_car()

    if pet.ycor() > 300:
        pet.restart_pet()
        car.inc_speed()
        level.point()

    for car_single in car.all_car:
        if car_single.distance(pet) < 20:
            level.gameOver()
            is_game_on = False

screen.exitonclick()
