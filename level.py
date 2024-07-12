from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-280, 245)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def point(self):
        self.score += 1
        self.update_score()

    def gameOver(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
