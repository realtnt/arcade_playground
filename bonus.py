import random

import arcade

from constants import *


class Bonus(arcade.Sprite):
    def __init__(self) -> None:
        self.bonus_texture = arcade.load_texture(":resources:/images/items/gold_1.png")
        super().__init__(self.bonus_texture, scale=SPRITE_SCALING)

        self.__current_scale = SPRITE_SCALING
        self.__duration = random.randint(4, 9)
        self.__time_alive = 0.0
        self.hit = False
        self.killed_player = False
        self.growth_factor = 0.0
        self.speed_x = random.randint(300, 500)
        self.speed_y = random.randint(200, 500) * random.choice([1, -1])

    def update(self, delta_time: float = 1 / 60) -> None:
        self.__time_alive += delta_time

        self.randomise_direction()

        self.center_x += self.speed_x * delta_time
        self.center_y -= self.speed_y * delta_time

        if self.center_x > WINDOW_WIDTH - self.width / 2:
            self.center_x = WINDOW_WIDTH - self.width / 2
            self.speed_x *= -1
        if self.center_x < self.width / 2:
            self.center_x = self.width / 2
            self.speed_x *= -1
        if self.center_y > WINDOW_HEIGHT - self.height / 2:
            self.center_y = WINDOW_HEIGHT - self.height / 2
            self.speed_y *= -1
        if self.center_y < self.height / 2:
            self.center_y = self.height / 2
            self.speed_y *= -1

        if self.growth_factor + BLOODCLOT_GROWTH_RATE > self.__current_scale:
            self.__current_scale += BLOODCLOT_GROWTH_RATE
            self.scale = self.__current_scale
            self.angle = self.angle + BLOODCLOT_ROTATION_SPEED

        if self.__time_alive > self.__duration:
            self.remove_from_sprite_lists()

    def randomise_direction(self):
        self.speed_x *= random.choice(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
        )
        self.speed_y *= random.choice([1, 1, 1, 1, 1, 1, 1, -1])
