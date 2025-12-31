import arcade

from constants import *


class Bloodclot(arcade.Sprite):
    def __init__(self, texture) -> None:
        super().__init__(texture, scale=SPRITE_SCALING)
        self.hit = False
        self.killed_player = False
        self.growth_factor = 0.0
        self.__current_scale = SPRITE_SCALING

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x -= self.change_x
        
        if self.growth_factor + BLOODCLOT_GROWTH_RATE > self.__current_scale:
            self.__current_scale += BLOODCLOT_GROWTH_RATE
            self.scale = self.__current_scale
            self.angle = self.angle + BLOODCLOT_ROTATION_SPEED
        
        if self.left < -self.width:
            self.remove_from_sprite_lists()
