import pygame as pg
from pygame import QUIT

# Create a new file snake2.py
# start from scratch and create a game
# ask for the size of the board in pixels
# ask for the number of grid in the board
# it draws the board with the grids
# it draws the head of the snake in the center of the board


# board_width = int(input("Please input the size of the board: "))
# num_grids = int(input("Please input the number of grids on the board: "))
board_width = 500
num_grids = 25
grid_width = board_width // num_grids

# init pygame
pg.init()
screen = pg.display.set_mode((board_width, board_width))

def draw_snake(x, y):
    pg.draw.rect(screen, (0, 255, 0), (grid_width * x, grid_width * y, grid_width, grid_width))


while True:
    # get message
    for event in pg.event.get():
        if event.type == QUIT:
            break

    # draw grids
    for i in range(1, num_grids):
        pg.draw.line(screen, (255, 255, 255), (0, grid_width * i), (board_width, grid_width * i))
        pg.draw.line(screen, (255, 255, 255), (grid_width * i, 0), (grid_width * i, board_width))

    # draw snake
    draw_snake(num_grids // 2, num_grids // 2)

    pg.display.flip()
    pg.time.wait(10)

input("Type anything")
