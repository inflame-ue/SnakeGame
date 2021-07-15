# TODO: 1. Create a snake body:

# Import modules:
import turtle
import time
import snake
import food
import scoreboard

# Screen setup:
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen tracer


# Snake setup:
snake = snake.Snake()  # Snake object from Snake class.
food = food.Food()
score = scoreboard.ScoreBoard()

# End of block one.

# TODO: 3. Bind controls for the snake:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO: 2. Move the snake.

# Stop variable:
game_is_on = True

# While loop that moves the snake:
while game_is_on:

    # Set screen refresh for 0.1 second:
    screen.update()
    time.sleep(0.1)

    # Move the snake.
    snake.move_the_snake()  # snake method.

    # Detect collision with food:

    if snake.list_of_snakes[0].distance(food) < 15:
        score.clear_the_screen()
        score.track_score()
        food.refresh()


# Exit on click:
screen.exitonclick()
