from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.write(f"SCORE: {self.left_score}:{self.right_score}",
               move=False, align='center', font=('Arial', 22, 'normal'))

    def scoreboard_update(self):
        self.clear()
        self.write(f"SCORE: {self.left_score}:{self.right_score}",
                   move=False, align='center', font=('Arial', 22, 'normal'))

    def scoring(self, side):
        if side == "right":
            self.right_score += 1
        elif side == "left":
            self.left_score += 1
