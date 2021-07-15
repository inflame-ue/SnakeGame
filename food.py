# TODO: 4. Create food class and detect collisions with food.

# Importing turtle and random:
import turtle
import random


# Creating new food class:
class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    # New random position of the food:
    def refresh(self):
        """Moves food to the next random position on the screen."""
        x = random.choice(range(-280, 280, 20))
        y = random.choice(range(-280, 280, 20))
        self.goto(x, y)
