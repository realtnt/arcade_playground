import random

import arcade

import bloodclot
import bullet
import player
import starfield
import virus
from constants import *


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.time_since_last_virus = 0.0
        self.time_since_last_bloodclot = 0.0
        self.bullets_allowed = 40
        self.directions = {"up": False, "down": False, "left": False, "right": False}
        self.starfield = starfield.Starfield()
        self.bullet_list = arcade.SpriteList()
        self.sprites = arcade.SpriteList()
        self.bloodclot_list = arcade.SpriteList()
        self.virus_list = arcade.SpriteList()

    def setup(self) -> None:
        self.bullet_texture = arcade.load_texture(
            ":resources:/images/space_shooter/laserBlue01.png"
        )
        self.bloodclot_texture = arcade.load_texture(
            ":resources:/images/enemies/saw.png"
        )
        self.virus_texture = arcade.load_texture(
            ":resources:/images/enemies/wormGreen_move.png"
        )
        self.create_player()

    def create_player(self) -> None:
        self.player_texture = arcade.load_texture(
            ":resources:/images/space_shooter/playerShip3_orange.png"
        ).rotate_90()
        self.player = player.Player(self.player_texture)
        self.player.position = (
            150,
            WINDOW_HEIGHT / 2 - self.player.height / 2,
        )
        self.sprites.append(self.player)

    def on_draw(self) -> None:
        self.clear()
        self.starfield.draw()
        self.sprites.draw()
        self.bullet_list.draw()
        self.virus_list.draw()
        self.bloodclot_list.draw()

    def on_update(self, delta_time) -> None:
        self.starfield.update(delta_time)
        self.sprites.update()
        self.bullet_list.update()

        self.time_since_last_virus += delta_time
        if self.time_since_last_virus >= 1.0:
            self.time_since_last_virus = 0.0
            self.spawn_virus()
        self.virus_list.update()
        
        self.time_since_last_bloodclot += delta_time
        if self.time_since_last_bloodclot >= 2.5:
            self.time_since_last_bloodclot = 0.0
            self.spawn_bloodclot()
        self.bloodclot_list.update()

        virus_hit_list = arcade.check_for_collision_with_list(
            self.player, self.virus_list
        )

        for virus_hit in virus_hit_list:
            virus_hit.remove_from_sprite_lists()

        for bullet_hit in self.bullet_list:
            bullet_hit_list = arcade.check_for_collision_with_list(
                bullet_hit, self.virus_list
            )

            for virus_hit in bullet_hit_list:
                virus_hit.remove_from_sprite_lists()
                bullet_hit.remove_from_sprite_lists()

    def update_player_speed(self) -> None:
        self.player.change_x = 0
        self.player.change_y = 0

        if self.directions["left"] and not self.directions["right"]:
            self.player.change_x = -MOVEMENT_SPEED
        if self.directions["right"] and not self.directions["left"]:
            self.player.change_x = MOVEMENT_SPEED
        if self.directions["up"] and not self.directions["down"]:
            self.player.change_y = MOVEMENT_SPEED
        if self.directions["down"] and not self.directions["up"]:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.directions["up"] = True
            self.update_player_speed()
        if symbol == arcade.key.DOWN:
            self.directions["down"] = True
            self.update_player_speed()
        if symbol == arcade.key.LEFT:
            self.directions["left"] = True
            self.update_player_speed()
        if symbol == arcade.key.RIGHT:
            self.directions["right"] = True
            self.update_player_speed()
        if symbol == arcade.key.SPACE and len(self.bullet_list) < self.bullets_allowed:
            self.fire_bullet()
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.directions["up"] = False
            self.update_player_speed()
        if symbol == arcade.key.DOWN:
            self.directions["down"] = False
            self.update_player_speed()
        if symbol == arcade.key.LEFT:
            self.directions["left"] = False
            self.update_player_speed()
        if symbol == arcade.key.RIGHT:
            self.directions["right"] = False
            self.update_player_speed()

    def fire_bullet(self) -> None:
        self.bullet = bullet.Bullet(self.bullet_texture)
        self.bullet.position = (
            self.player.center_x,
            self.player.center_y,
        )
        self.bullet_list.append(self.bullet)
        self.bullet.change_x = BULLET_SPEED

    def spawn_virus(self) -> None:
        self.virus = virus.Virus(self.virus_texture)
        self.virus.position = (
            WINDOW_WIDTH + self.virus.width,
            random.randint(
                int(self.virus.height), int(WINDOW_HEIGHT - self.virus.height)
            ),
        )
        self.virus_list.append(self.virus)
        self.virus.change_x = VIRUS_SPEED

    def spawn_bloodclot(self) -> None:
        self.bloodclot = bloodclot.Bloodclot(self.bloodclot_texture)
        self.bloodclot.position = (
            WINDOW_WIDTH + self.bloodclot.width,
            random.randint(
                int(self.virus.height), int(WINDOW_HEIGHT - self.virus.height)
            ),
        )
        self.bloodclot_list.append(self.bloodclot)
        self.bloodclot.change_x = BLOODCLOT_SPEED


def main() -> None:
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.center_window()
    game = GameView()
    game.setup()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
