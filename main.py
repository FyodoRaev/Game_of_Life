import pygame
import game_functions as gf
from random import randint
from copy import deepcopy
from settings import Settings
from ourgrid import Grid


def run_game():
    pygame.init()
    game_settings = Settings()
    grid = Grid()
    surface = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game of Life")
    while True:
        gf.check_events()
        surface.fill(pygame.Color('white'))
    

        [pygame.draw.line(surface, pygame.Color('black'), (x, 0), (x, game_settings.screen_height)) for x in range(0, game_settings.screen_width, grid.TILE)]
        [pygame.draw.line(surface, pygame.Color('black'), (0, y), (game_settings.screen_width, y)) for y in range(0, game_settings.screen_height, grid.TILE)]
        # draw life
        for x in range(1, grid.W - 1):
            for y in range(1, grid.H - 1):
                if grid.current_field[y][x]:
                  pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * grid.TILE + 2, y * grid.TILE + 2, grid.TILE - 2, grid.TILE - 2))
                grid.next_field[y][x] = gf.check_cell(grid.current_field, x, y)

        grid.current_field = deepcopy(grid.next_field)

        print(clock.get_fps())
        pygame.display.flip()
        clock.tick(game_settings.fps)

run_game()


