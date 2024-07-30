from turtle import Turtle
BALL_COLOR = "black"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        '''Automatically moves the ball'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        '''Bounces the ball while it hits a paddle'''
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        '''Bounces the ball while it hits the celling or bottom'''
        self.y_move *= -1

    def reset_pos(self):
        '''Returns the ball the the center'''
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
          