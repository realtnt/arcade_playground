import arcade
from constants import *

class Player(arcade.Sprite):
    def __init__(self, texture) -> None:
        super().__init__(texture, scale=SPRITE_SCALING)
        self.lives = LIVES
        self.score = 0
        self.multiplier = 1

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.left < 0:
            self.left = 0
        elif self.right > WINDOW_WIDTH - 1:
            self.right = WINDOW_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > WINDOW_HEIGHT - 1:
            self.top = WINDOW_HEIGHT - 1