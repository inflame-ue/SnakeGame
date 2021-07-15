# TODO: 4. Create food class and detect collisions with food.

# Importing turtle and random:
import turtle
import random


# Creating new food class:
class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    # New random position of the food:
    def refresh(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)
