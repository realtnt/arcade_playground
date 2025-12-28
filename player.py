import arcade
from constants import * # noqa: F403

class Player(arcade.Sprite):
    def __init__(self, left_texture, right_texture):
        super().__init__(right_texture, scale=SPRITE_SCALING)
        self.textures.append(left_texture)

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_RIGHT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_LEFT]
