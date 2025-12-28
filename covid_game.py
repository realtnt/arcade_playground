import arcade

import starfield
import player
from constants import *



class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.directions = {"up": False, "down": False, "left": False, "right": False}

        self.player_height = 30
        self.player_width = 55
        self.player_x = 10
        self.player_y = WINDOW_HEIGHT // 2 - self.player_height // 2

        self.starfield = starfield.Starfield()

        self.left_texture = arcade.load_texture(":resources:images/enemies/bee.png")
        self.right_texture = self.left_texture.flip_left_right()

        self.sprites = arcade.SpriteList()
        self.player_sprite = player.Player(self.left_texture, self.right_texture)
        
        
        
        self.player_sprite.position = (50, WINDOW_HEIGHT / 2 - self.player_sprite.height / 2)
        self.sprites.append(self.player_sprite)

    def on_draw(self) -> None:
        self.clear()
        self.starfield.draw()
        self.sprites.draw()

    def on_update(self, delta_time) -> None:
        self.starfield.update(delta_time)
        self.sprites.update()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        if symbol == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        if symbol == arcade.key.SPACE:
            print("fire")
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.player_sprite.change_y = 0
        if symbol == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main() -> None:
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.center_window()
    game = GameView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
