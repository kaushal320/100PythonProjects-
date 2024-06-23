import turtle
from turtle import Turtle

ALIGNMENT: str = "center"
FONT = ('Arial', 22, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)

    def update_score_board(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
