from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", move=False, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 240)
        self.write(f"{self.r_score}", move=False, align="center", font=("Arial", 40, "normal"))
        self.hideturtle()

    def update_l_Score(self):
        self.l_score+=1
        self.show_score()

    def update_r_Score(self):
        self.r_score+=1
        self.show_score()
