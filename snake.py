# TODO: 3. Create a snake class:

# Import module:
import turtle
import constants


# Create a new class:
class Snake:

    # Initialize(create a snake):
    def __init__(self):
        self.list_of_snakes = []
        self.create_snake()

    def create_snake(self):
        """Creates a starting body for the snake."""
        for position in constants.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds new segment to the snake."""
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.list_of_snakes.append(snake)

    # Add new segments to the snake:
    def extend(self):
        """Extends the body of the snake."""
        self.add_segment(self.list_of_snakes[-1].position())

    # Move the snake:
    def move_the_snake(self):
        """Moves the whole snake forward."""
        for number in range(len(self.list_of_snakes) - 1, 0, -1):
            new_position = self.list_of_snakes[number - 1].position()
            self.list_of_snakes[number].goto(new_position)

        self.list_of_snakes[0].fd(constants.MOVE_SPEED)

    def reset(self):
        for segment in self.list_of_snakes:
            segment.goto(1000, 1000)
        self.list_of_snakes.clear()
        self.create_snake()

    def up(self):
        """Sets heading to up."""
        if self.list_of_snakes[0].heading() != constants.HEADINGS[3]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[1])

    def down(self):
        """Sets heading to down."""
        if self.list_of_snakes[0].heading() != constants.HEADINGS[1]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[3])

    def left(self):
        """Sets heading to left."""
        if self.list_of_snakes[0].heading() != constants.HEADINGS[0]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[2])

    def right(self):
        """Sets heading to right."""
        if self.list_of_snakes[0].heading() != constants.HEADINGS[2]:
            self.list_of_snakes[0].setheading(constants.HEADINGS[0])
