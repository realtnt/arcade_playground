import random

import arcade

from constants import *


class Bloodclot(arcade.Sprite):
    def __init__(self, texture) -> None:
        super().__init__(texture, scale=SPRITE_SCALING)

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x -= self.change_x
        self.center_y = random.randint(0, WINDOW_HEIGHT)
        
        if self.left < 0:
            self.remove_from_sprite_lists()
