from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
            print(self.high_score)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score :{self.score}  High Score :{self.high_score}", move=False, align="center", font=("Arial", 22, "normal"))
        self.hideturtle()


    def update_score(self):
        self.score+=1
        self.show_score()

    def game_over(self):
        if self.score > self.high_score:
            x = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(x))

        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over Your Score is {self.score}  High Score :{self.high_score}", align="center", move=False, font=("Arial", 20, "normal"))
