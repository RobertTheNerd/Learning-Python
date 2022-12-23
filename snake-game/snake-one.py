import pygame as pg

board_size = 500
num_grid = 25

def draw_grid(surface, n):
    segment_width = board_size // n

    # draw vertical lines
    for i in range(1, n):
        pg.draw.line(surface, (255, 255, 255), (segment_width * i, 0), (segment_width * i, board_size - 1))

    # draw horizontal lines
    for i in range(1, n):
        pg.draw.line(surface, (255, 255, 255), (0, segment_width * i), (board_size - 1, segment_width * i))


pg.init()
screen = pg.display.set_mode((board_size, board_size))

# draw_grid(screen, num_grid)
# pg.draw.line(screen, (255, 255, 255), (0, 50), (499, 50))
# pg.draw.line(screen, (255, 255, 255), (50, 0), (50, 499))

# pg.draw.circle(screen, (255, 255, 255), (50, 50), 1)
# pg.draw.circle(screen, (255, 255, 255), (100, 100), 1)
# pg.draw.circle(screen, (255, 255, 255), (250, 250), 1)

for i in range(1, 10):
    pg.draw.circle(screen, (255, 255, 255), (50 * i, 50 * i), 1)




pg.display.flip()

input("type something")