import pygame

width = 500
rows = 20

def init_game():
    global screen
    pygame.init()
    screen = pygame.display.set_mode([width, width])


def draw_lines(surface):
    grid_width = width // rows

    for i in range(1, rows):
        pygame.draw.line(surface, (255, 255, 255), (grid_width * i, 0), (grid_width * i, width))
        pygame.draw.line(surface, (255, 255, 255), (0, grid_width * i), (width, grid_width * i))


def game():
    init_game()

    while True:
        draw_lines(screen)
        pygame.display.update()
        pygame.time.delay(50)
        pass


game()
