from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('green')
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_food()

    def new_food(self):
        x_random = random.randint(-270, 270)
        y_random = random.randint(-270, 270)
        self.goto(x_random, y_random)
