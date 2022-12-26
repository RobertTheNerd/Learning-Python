from enum import Enum

import pygame as pg
from pygame import QUIT

# Create a new file snake2.py
# start from scratch and create a game
# ask for the size of the board in pixels
# ask for the number of grid in the board
# it draws the board with the grids
# it draws the head of the snake in the center of the board


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


# board_width = int(input("Please input the size of the board: "))
# num_grids = int(input("Please input the number of grids on the board: "))
board_width = 500
num_grids = 25
grid_width = board_width // num_grids
snake_pos = (num_grids // 2, num_grids // 2)
snake_direction = Direction.RIGHT
move_delay = 250

# init pygame
pg.init()
screen = pg.display.set_mode((board_width, board_width))


def draw_snake(x, y):
    pg.draw.rect(screen, (0, 255, 0), (grid_width * x, grid_width * y, grid_width, grid_width))


while True:
    # get message
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                snake_direction = Direction.LEFT
            if event.key == pg.K_RIGHT:
                snake_direction = Direction.RIGHT
            if event.key == pg.K_UP:
                snake_direction = Direction.UP
            if event.key == pg.K_DOWN:
                snake_direction = Direction.DOWN

    # set background color
    screen.fill(0)

    # draw grids
    for i in range(1, num_grids):
        pg.draw.line(screen, (255, 255, 255), (0, grid_width * i), (board_width, grid_width * i))
        pg.draw.line(screen, (255, 255, 255), (grid_width * i, 0), (grid_width * i, board_width))

    # move the snake
    if snake_direction == Direction.LEFT:
        snake_pos = ((snake_pos[0] - 1) % num_grids, snake_pos[1])
    if snake_direction == Direction.RIGHT:
        snake_pos = ((snake_pos[0] + 1) % num_grids, snake_pos[1])
    if snake_direction == Direction.UP:
        snake_pos = (snake_pos[0], (snake_pos[1] - 1) % num_grids)
    if snake_direction == Direction.DOWN:
        snake_pos = (snake_pos[0], (snake_pos[1] + 1) % num_grids)

    # draw snake
    draw_snake(*snake_pos)

    pg.display.flip()
    pg.time.wait(move_delay)


input("Type anything")
