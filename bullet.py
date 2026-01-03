import arcade
from constants import *

class Bullet(arcade.Sprite):
    def __init__(self, texture) -> None:
        super().__init__(texture, scale=SPRITE_SCALING)

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.right > WINDOW_WIDTH - 1:
            self.remove_from_sprite_lists()