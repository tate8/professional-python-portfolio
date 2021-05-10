from turtle import Turtle


class Object(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)
        self.health = 100


