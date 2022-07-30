from turtle import Turtle, Screen
from game_machine import GameMachine
from score_board import ScoreBoard
screen = Screen()
screen.title("US State Guess Game")
shape = "blank_states_img.gif"
screen.addshape(shape)
screen.setup(width=740, height=500)

timmy = Turtle(shape)
score_board = ScoreBoard()
game_machine = GameMachine()

game_is_on = True

while game_is_on and score_board.score <50:
    state = screen.textinput(title=f"{score_board.score}/50 States Correct", prompt="Guess the name of Another state")

    if state.capitalize() == "Quit":
        game_is_on = False

    if game_machine.check_answer(state.capitalize()):
        game_machine.go_to(state.capitalize())
        score_board.increase_score()

screen.exitonclick()