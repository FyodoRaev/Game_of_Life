from settings import Settings
class Grid():
  def __init__(self):
    self.game_settings = Settings()
    self.TILE = 10
    self.W = self.game_settings.screen_width// self.TILE
    self.H = self.game_settings.screen_height // self.TILE
    self.next_field = [[0 for i in range(self.W)] for j in range(self.H)]
    self.current_field = [[0 for i in range(self.W)] for j in range(self.H)]
    self.current_field = [[1 if i == self.W // 2 or j == self.H // 2 else 0 for i in range(self.W)] for j in range(self.H)]
  

  