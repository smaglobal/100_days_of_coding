import random
from turtle import  Turtle

class Food (Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("brown")
        self.speed("fastest")
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)
        self.refresh()

    def refresh(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)
