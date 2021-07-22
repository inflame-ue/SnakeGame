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
        with open('data.txt', 'r') as self.file:
            self.high_score = int(self.file.read())
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}" f" High score: {self.high_score}", False, align="center", font=("Comic Sans MS", 15, "normal"))

    def track_score(self):
        """Tracks score and writes it on the screen."""
        self.score += 1
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as self.file:
                self.file.write(str(self.score))
            with open('data.txt', 'r') as self.file:
                self.high_score = int(self.file.read())
        self.score = 0
        self.scoreboard()
