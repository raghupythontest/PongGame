import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    def move(self):
        time.sleep(self.move_speed)
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9
    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()
