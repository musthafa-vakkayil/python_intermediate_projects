from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.level = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level :{self.level}", move=False, align="center", font=FONT)
        self.hideturtle()


    def update_level(self):
        self.level +=1
        self.show_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", move=False, align="center", font=FONT)
        self.hideturtle()
