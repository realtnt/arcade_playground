import arcade

from constants import *


class Virus(arcade.Sprite):
    def __init__(self, texture) -> None:
        super().__init__(texture, scale=SPRITE_SCALING)

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x -= self.change_x
        if self.left < -self.width:
            self.remove_from_sprite_lists()
            
