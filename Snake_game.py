import tkinter as tk
import random

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 170
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Snake class
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [] 
        self.squares = []

        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Food class
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Movement logic
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

# Direction change
def change_direction(new_direction):
    global direction

    if new_direction == "left" and direction != "right":
        direction = new_direction
    elif new_direction == "right" and direction != "left":
        direction = new_direction
    elif new_direction == "up" and direction != "down":
        direction = new_direction
    elif new_direction == "down" and direction != "up":
        direction = new_direction

# Collision detection
def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True

    return False

# Game over screen
def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       font=('consolas', 50), text="GAME OVER", fill="red")

# GUI setup
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Bindings
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Start
direction = "right"
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()