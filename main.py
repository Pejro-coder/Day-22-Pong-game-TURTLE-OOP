from turtle import Screen
from edge import Edge
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

edge = Edge()
ball = Ball()
scoreboard = Scoreboard()

paddle_right = Paddle("yellow", (380, 0))
paddle_left = Paddle("green", (-380, 0))

# paddle reset function, calls paddle left and right reset methods (when a player scores-scoreboard)
def paddles_reset():
    paddle_right.reset_position((380, 0))
    paddle_left.reset_position((-380, 0))

screen.listen()
screen.onkeypress(fun=paddle_right.up, key="Up")
screen.onkeypress(fun=paddle_right.down, key="Down")
screen.onkeypress(fun=paddle_left.up, key="w")
screen.onkeypress(fun=paddle_left.down, key="s")

game_is_one = True
right_left = [0, 180]
random.choice(right_left)
ball.reset_ball(random.choice(right_left))
screen.update()
time.sleep(1)

while game_is_one:
    screen.update()
    ball.move()
    time.sleep(0.005)

    # top border conditions for bounce
    if ball.ycor() > 280:
        if ball.heading() > 90 and ball.heading() < 180:
            ball.change_direction(225)
        elif ball.heading() > 0 and ball.heading() < 90:
            ball.change_direction(315)

    # bottom border conditions for bounce
    elif ball.ycor() < -280:
        if ball.heading() > 270 and ball.heading() < 360:
            ball.change_direction(45)
            print("yolo")
        elif ball.heading() > 180 and ball.heading() < 270:
            ball.change_direction(135)

    # scoreboard, ball reset, paddles reset. Score goes up if ball hits the right or the left edge
    if ball.xcor() > 390:
        scoreboard.scoring("left")
        time.sleep(1)
        ball.reset_ball(random.randint(170, 190))
        paddles_reset()
    elif ball.xcor() < -390:
        scoreboard.scoring("right")
        time.sleep(1)
        ball.reset_ball(random.randint(-10, 10))
        paddles_reset()
    scoreboard.scoreboard_update()

    # paddle hit detection
    if ball.xcor() > 365 and ball.distance(paddle_right) < 32:
        ball.change_direction(random.randint(120, 240))
        ball.increase_speed()
    elif ball.xcor() < -365 and ball.distance(paddle_left) < 32:
        ball.change_direction(random.randint(-60, 60))
        ball.increase_speed()

screen.exitonclick()
