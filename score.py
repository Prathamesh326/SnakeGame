from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updatescore()
        self.hideturtle()

    def updatescore(self):
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 15, 'normal'))


    def calculate_score(self):
        self.score += 1
        self.clear()
        self.updatescore()
