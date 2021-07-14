# TODO: 3. Create a snake class:

# Import module:
import turtle
import constants


# Create a new class:
class Snake:

    # Initialize(create a snake):
    def __init__(self):
        self.list_of_snakes = []
        self.xcor = 0.0
        self.new_position = 0
        self.create_snake()

    def create_snake(self):
        for number in range(0, 3):
            snake = turtle.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setx(self.xcor)
            self.xcor -= 20
            self.list_of_snakes.append(snake)

    # Move the snake:
    def move_the_snake(self):

        for number in range(len(self.list_of_snakes) - 1, 0, -1):
            self.new_position = self.list_of_snakes[number - 1].position()
            self.list_of_snakes[number].goto(self.new_position)

        self.list_of_snakes[0].fd(constants.MOVE_SPEED)

    def up(self):

        if self.list_of_snakes[0].heading() != constants.HEADINGS[3]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[1])

    def down(self):

        if self.list_of_snakes[0].heading() != constants.HEADINGS[1]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[3])

    def left(self):

        if self.list_of_snakes[0].heading() != constants.HEADINGS[0]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[2])

    def right(self):

        if self.list_of_snakes[0].heading() != constants.HEADINGS[2]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[0])
