from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("OrangeRed")
        self.penup()
        self.velocity = 1.5

    def move(self):
        self.forward(self.velocity)

    def increase_speed(self):
        self.velocity += 0.1

    def change_direction(self, direction):
        self.setheading(direction)

    def reset_ball(self, direction):
        self.setposition(0, 0)
        self.setheading(direction)
        self.velocity = 1.5
