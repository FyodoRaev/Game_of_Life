import pygame
import game_functions as gf
from random import randint
from copy import deepcopy
from settings import Settings
from ourgrid import Grid

class Game_of_Life:
    def __init__(self):
      pygame.init()
      pygame.display.set_caption("Game of Life")
      self.game_settings = Settings()
      self.grid = Grid()
      self.surface = pygame.display.set_mode((self.game_settings.screen_width, self.game_settings.screen_height))
      self.clock = pygame.time.Clock()
    def run_game(self):
        while True:
            gf.check_events()
            self.surface.fill(pygame.Color('white'))  
            [pygame.draw.line(self.surface, pygame.Color('black'), (x, 0), (x, self.game_settings.screen_height)) for x in range(0, self.game_settings.screen_width, self.grid.TILE)]
            [pygame.draw.line(self.surface, pygame.Color('black'), (0, y), (self.game_settings.screen_width, y)) for y in range(0, self.game_settings.screen_height, self.grid.TILE)]
        # draw life
            for x in range(1, self.grid.W - 1):
                for y in range(1, self.grid.H - 1):
                    if self.grid.current_field[y][x]:
                      pygame.draw.rect(self.surface, pygame.Color('forestgreen'), (x * self.grid.TILE + 2, y * self.grid.TILE + 2, self.grid.TILE - 2, self.grid.TILE - 2))
                    self.grid.next_field[y][x] = gf.check_cell(self.grid.current_field, x, y)

            self.grid.current_field = deepcopy(self.grid.next_field)

            print(self.clock.get_fps())
            pygame.display.flip()
            self.clock.tick(self.game_settings.fps)

game = Game_of_Life()
game.run_game()




