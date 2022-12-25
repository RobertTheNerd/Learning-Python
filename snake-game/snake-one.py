import pygame as pg

board_size = 500
num_grid = 20


def draw_grid(surface, n):
    segment_width = board_size // n

    for i in range(1, n):
        # draw vertical lines
        pg.draw.line(surface, (255, 255, 255), (segment_width * i, 0), (segment_width * i, board_size - 1))
        # draw horizontal lines
        pg.draw.line(surface, (255, 255, 255), (0, segment_width * i), (board_size - 1, segment_width * i))


def draw_snake_head(surface, x, y):
    grid_width = board_size // num_grid
    snake_width = board_size // num_grid - 3
    pg.draw.rect(surface, (0, 250, 0), (grid_width * x + 2, grid_width * x + 2, snake_width, snake_width))

    pass


pg.init()
screen = pg.display.set_mode((board_size, board_size))

draw_grid(screen, num_grid)
draw_snake_head(screen, 3, 1)

pg.display.flip()

input("type something")
