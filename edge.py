from turtle import Turtle

SIDES = "RoyalBlue"
GOAL = "black"

X_COR = 390
Y_COR = 290


class Edge(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(6)
        self.penup()
        self.pencolor(SIDES)
        self.goto(-X_COR, Y_COR)
        self.pendown()
        self.goto(X_COR, Y_COR)
        self.pencolor(GOAL)
        self.goto(X_COR, -Y_COR)
        self.pencolor(SIDES)
        self.goto(-X_COR, -Y_COR)
        self.pencolor(GOAL)
        self.goto(-X_COR, Y_COR)
        self.pencolor(SIDES)

        self.goto(0, 290)
        self.setheading(270)

        for a in range(0, 10):
            self.penup()
            self.forward(16)
            self.pendown()
            self.forward(40)
