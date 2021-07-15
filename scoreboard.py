# TODO: 5. Create a scoreboard class and track the score.

# Importing modules:
import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, align="center", font=("Comic Sans MS", 15, "normal"))

    def track_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Comic Sans MS", 15, "normal"))

    def clear_the_screen(self):
        self.clear()
