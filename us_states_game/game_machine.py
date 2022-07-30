import pandas as pd
from turtle import Turtle


class GameMachine:

    def __init__(self):
        self.data = pd.read_csv("50_states.csv")
        self.states = self.data["state"]
        self.correct_answers = []

    def check_answer(self, answer):
        if answer not in self.correct_answers:
            for i in self.states:
                if i == answer:
                    self.correct_answers.append(answer)
                    return True
            else:
                return False

    def go_to(self, answer):
        x = self.data[self.data["state"] == answer]["x"]
        y = self.data[self.data["state"] == answer]["y"]
        timmy = Turtle()
        timmy.penup()
        timmy.goto(float(x), float(y))
        timmy.write(answer)
        timmy.hideturtle()
