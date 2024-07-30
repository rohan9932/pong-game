'''
    Steps: 
        1. Set up the main screen
        2. Create and move the paddle
        3. Create another paddle
        4. Create the ball and make it move
        5. Detect collision with the wall and make it bounce if it collides with the bottom wall
        6. Detect when paddle misses
        7. Make update score

    Needed classes:
        1. Paddle class // paddle.py
        2. Ball class // ball.py
        3. Dash line class 
        4. Scoreboard class // scoreboard.py

'''

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width= 800, height=600)
screen.title("Rohan's Pong Game")
screen.bgcolor("PeachPuff")
screen.tracer(0)

game_point = int(screen.textinput(title= "Game Round", prompt= "What should be the game point?"))

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
# right key controls
screen.onkey(r_paddle.up, "Up") 
screen.onkey(r_paddle.down, "Down")
# left key controls
screen.onkey(l_paddle.up, "w") 
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collsion with the paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect when r_paddle miss the ball
    if ball.xcor() > 390:
        ball.reset_pos()
        scoreboard.l_point()

    # Detect when l_paddle miss the ball
    if ball.xcor() < -390:
        ball.reset_pos()
        scoreboard.r_point()

    # Exit on gamepoint
    if scoreboard.l_score == game_point or scoreboard.r_score == game_point:
        game_is_on = False
        if scoreboard.l_score == game_point:
            scoreboard.win("Left")
        else:
            scoreboard.win("Right")


screen.exitonclick()
