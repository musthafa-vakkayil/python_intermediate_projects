from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong The Famous Arcade Game")

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
board = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detecting Collision With Wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddle
    if (ball.xcor() > 330 and ball.distance(paddle1) < 50 ) or (ball.xcor() < -330 and ball.distance(paddle2) < 50):
        ball.bounce_x()



    # Detect the ball is missed

    # detect with right paddle
    if ball.xcor() > 360:
        ball.reset_position()
        board.update_l_Score()

    # detect with left paddle
    if ball.xcor() < -360:
        ball.reset_position()
        board.update_r_Score()
screen.exitonclick()