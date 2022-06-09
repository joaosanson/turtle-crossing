from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard:
    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.goto(x=0, y=260)
        self.tim.color('black')
        self.score = 0
        self.points()

    def points(self):
        self.tim.clear()
        self.tim.goto(x=0, y=260)
        self.tim.write(f'SCORE: {self.score}', align="center", font=FONT)
        self.score += 1

    def finished(self):
        self.tim.clear()
        self.tim.goto(x=0, y=0)
        self.tim.write(f'SCORE: {self.score-1}', align="center", font=FONT)
