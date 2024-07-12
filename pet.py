from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Pet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        # new_ycor = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_ycor)
        self.forward(MOVE_DISTANCE)

    def restart_pet(self):
        self.goto(STARTING_POSITION)
