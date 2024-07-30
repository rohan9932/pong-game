from turtle import Turtle
PADDLE_COLOR = "Black"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == "right":
            self.goto(350, 0)
        elif position == "left":
            self.goto(-350, 0)

    def up(self):
        '''Moves the paddle upwords'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        '''Moves the paddle downwords'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        