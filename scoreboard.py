from turtle import Turtle
SCOREBOARD_COLOR = "black"
ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")
WIN_TITLE_FONT = ("Chalkboard SE", 35, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0 
        self.update_scoreboard()      

    def update_scoreboard(self):
        '''Updates the scoreboard while anyone scores a point'''
        self.clear()
        self.goto(-60, 200)
        self.write(self.l_score, move= True, align= ALIGNMENT, font= FONT)
        self.goto(60, 200)
        self.write(self.r_score, move= ALIGNMENT, font= FONT)

    def l_point(self):
        '''Increases the point of the left user'''
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        '''Increases the point of the right user'''
        self.r_score += 1
        self.update_scoreboard()

    def win(self, winner):
        '''Declares the winner'''
        self.goto(0, 0)
        self.write(f"{winner} user has won!", move= True, align= ALIGNMENT, font= WIN_TITLE_FONT)
