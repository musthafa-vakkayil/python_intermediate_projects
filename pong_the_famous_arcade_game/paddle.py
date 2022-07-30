from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,cor):
        super().__init__()
        self.create_paddle(cor)

    def create_paddle(self, cor):
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(cor)

    def up(self):
        x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x, new_y)

    def down(self):
        x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x, new_y)

