# Antardip Himel

# Run this on terminal
# cd /Users/himel/PycharmProjects/SnakeGame
# python3 Snake.py

import random  # Import the random module to randomly place food
import curses  # Import the curses module for handling the terminal interface

# Initialize the curses screen
s = curses.initscr()
curses.curs_set(0)  # Hide the default cursor
sh, sw = s.getmaxyx()  # Get the height (sh) and width (sw) of the terminal window
w = curses.newwin(sh, sw, 0, 0)  # Create a new window for the game
w.keypad(1)  # Enable keypad input (arrow keys)
w.timeout(100)  # Set a timeout of 100 milliseconds for each input (game speed)

# Set initial position of the snake in the middle-left of the screen
snk_x = sw // 4  # Snake's starting x-coordinate
snk_y = sh // 2  # Snake's starting y-coordinate
snake = [
    [snk_y, snk_x],      # Head of the snake
    [snk_y, snk_x - 1],  # Body segment 1
    [snk_y, snk_x - 2]   # Body segment 2
]

# Place the food initially in the middle of the screen
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Display the food on the screen (ASCII pie symbol)

key = curses.KEY_RIGHT  # Start the game with the snake moving to the right

# Main game loop
while True:
    next_key = w.getch()  # Capture the next key press
    key = key if next_key == -1 else next_key  # If no key is pressed, continue with the current direction

    # Check for collisions with the walls or self
    if (snake[0][0] in [0, sh - 1] or  # If snake hits the top or bottom wall
        snake[0][1] in [0, sw - 1] or  # If snake hits the left or right wall
        snake[0] in snake[1:]):        # If snake hits itself
        curses.endwin()  # End the curses window session
        quit()  # Quit the game

    # Create a new head for the snake based on the direction of movement
    new_head = [snake[0][0], snake[0][1]]  # Copy the position of the current head

    # Update the head's position based on the key pressed (arrow keys)
    if key == curses.KEY_DOWN:
        new_head[0] += 1  # Move down by increasing the y-coordinate
    if key == curses.KEY_UP:
        new_head[0] -= 1  # Move up by decreasing the y-coordinate
    if key == curses.KEY_LEFT:
        new_head[1] -= 1  # Move left by decreasing the x-coordinate
    if key == curses.KEY_RIGHT:
        new_head[1] += 1  # Move right by increasing the x-coordinate

    # Insert the new head at the beginning of the snake
    snake.insert(0, new_head)

    # Check if the snake eats the food
    if snake[0] == food:
        food = None  # Remove the current food
        # Generate new food in a random position that is not occupied by the snake
        while food is None:
            nf = [
                random.randint(1, sh - 2),  # Random y-coordinate for food
                random.randint(1, sw - 2)   # Random x-coordinate for food
            ]
            food = nf if nf not in snake else None  # Ensure food doesn't overlap the snake
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Display new food
    else:
        # If no food is eaten, move the snake forward by removing the tail
        tail = snake.pop()  # Remove the last segment of the snake (tail)
        w.addch(int(tail[0]), int(tail[1]), ' ')  # Erase the tail from the screen

    # Draw the new head of the snake on the screen
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)  # Display the snake's head as a block character


# Explanation of the Code in Comments:

# Import Modules:
# random: Used for generating random coordinates for the food.
# curses: Used for handling terminal graphics and inputs.

# Initialize Curses and the Game Window:
# curses.initscr() starts the curses screen.
# The snake and food are displayed inside a window that fills the terminal.
# Cursor is hidden, and a timeout is set to control the game speed.

# Snake Initialization:
# The snake is represented by a list of coordinates, with the head being the first element.
# The snake starts at the middle-left part of the screen.

# Food Initialization:
# The food is placed at the center of the screen at the start of the game.
# The food is represented by an ASCII symbol (curses.ACS_PI).

# Game Loop:
# The game keeps running in an infinite loop until the player loses.
# The snake moves in the direction of the arrow key pressed by the player.
# The game checks for collisions with the walls or the snake's body.

# Snake Movement:
# The snake's head moves in the direction based on the key pressed.
# The rest of the body follows the head.

# Food Eating Logic:
# If the snake's head reaches the food, it grows (the tail is not removed).
# New food is placed at a random location that doesn't overlap the snake's body.

# Collision Detection:
# The game ends if the snake hits a boundary or itself.

# Drawing on Screen:
# The snake's position is updated on the screen with each movement.
# The food is redrawn at a new position after it’s eaten.
