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
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Comic Sans MS", 15, "normal"))

    def track_score(self):
        """Tracks score and writes it on the screen."""
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        """Writes on the screen game over."""
        self.setposition(0, 0)
        self.write("GAME OVER", False, align="center", font=("Comic Sans MS", 15, "normal"))
