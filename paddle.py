from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, color, x_cord):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2.5, outline=None)
        self.color(color)
        self.setheading(90)
        self.goto(x_cord)

    def reset_position(self, x_cord):
        self.goto(x_cord)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
