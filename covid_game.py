import random

import arcade

import bloodclot as bc
import bonus as bn
import bullet as b
import player as p
import starfield
import virus as v
from constants import *


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.time_since_last_virus = 0.0
        self.time_since_last_bloodclot = 0.0
        self.time_since_last_bonus = 0.0
        self.time_since_last_powerup = 0.0
        self.bullets_allowed = 40
        self.directions = {"up": False, "down": False, "left": False, "right": False}
        self.starfield = starfield.Starfield()
        self.bullet_list = arcade.SpriteList()
        self.player_sprite = arcade.SpriteList()
        self.bloodclot_list = arcade.SpriteList()
        self.bonus_list = arcade.SpriteList()
        self.virus_list = arcade.SpriteList()
        self.total_bullets = 1
        self.virus_spawning_freq = 1.0
        self.bloodclot_spawning_freq = 2.5
        self.bonus_spawning_freq = 4.0
        self.powerup_spawning_freq = 3.5

    def setup(self) -> None:
        self.bonus_texture = arcade.load_texture(
            ":resources:/images/items/gold_1.png"
        )
        
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
        self.player = p.Player(self.player_texture)
        self.player.position = (
            150,
            WINDOW_HEIGHT / 2 - self.player.height / 2,
        )
        self.player_sprite.append(self.player)

    def on_draw(self) -> None:
        self.clear()
        self.starfield.draw()
        self.player_sprite.draw()
        self.bullet_list.draw()
        self.virus_list.draw()
        self.bloodclot_list.draw()
        self.bonus_list.draw()

        arcade.draw_text(
            f"Score: {self.player.score}", 20, WINDOW_HEIGHT - 20, arcade.color.WHITE, 12
        )
        arcade.draw_text(
            f"Lives: {self.player.lives}", 20, WINDOW_HEIGHT - 40, arcade.color.WHITE, 12
        )
        arcade.draw_text(
            f"Bullets: {self.total_bullets}",
            20,
            WINDOW_HEIGHT - 60,
            arcade.color.WHITE,
            12,
        )

    def on_update(self, delta_time) -> None:
        self.spawn_virus(delta_time)
        self.spawn_bloodclot(delta_time)
        self.spawn_bonus(delta_time)
        
        self.starfield.update(delta_time)
        self.player_sprite.update()
        self.bullet_list.update()
        self.virus_list.update()
        self.bloodclot_list.update()
        self.bonus_list.update()

        self.check_player_collisions()
        self.check_bullet_collisions()

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
        if symbol == arcade.key.P:
            if self.total_bullets < 7:
                self.total_bullets += 1
        if symbol == arcade.key.L:
            if self.total_bullets > 1:
                self.total_bullets -= 1

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
        for i in range(1, self.total_bullets + 1):
            self.bullet = b.Bullet(self.bullet_texture)
            self.bullet.position = (
                self.player.center_x,
                self.player.center_y
                + self.total_bullets * BULLETS_GAP // 2
                - (i - 1) * BULLETS_GAP
                - BULLETS_GAP // 2,
            )
            self.bullet_list.append(self.bullet)
            self.bullet.change_x = BULLET_SPEED

    def spawn_virus(self, delta_time) -> None:
        self.time_since_last_virus += delta_time
        if self.time_since_last_virus >= self.virus_spawning_freq:
            self.time_since_last_virus = 0.0

            self.virus = v.Virus(self.virus_texture)
            self.virus.position = (
                WINDOW_WIDTH + self.virus.width,
                random.randint(
                    int(self.virus.height), int(WINDOW_HEIGHT - self.virus.height)
                ),
            )
            self.virus_list.append(self.virus)
            self.virus.change_x = VIRUS_SPEED

    def spawn_bloodclot(self, delta_time) -> None:
        self.time_since_last_bloodclot += delta_time
        if self.time_since_last_bloodclot >= self.bloodclot_spawning_freq:
            self.time_since_last_bloodclot = 0.0

            self.bloodclot = bc.Bloodclot(self.bloodclot_texture)
            self.bloodclot.position = (
                WINDOW_WIDTH + self.bloodclot.width,
                random.randint(
                    int(self.virus.height), int(WINDOW_HEIGHT - self.virus.height)
                ),
            )
            self.bloodclot_list.append(self.bloodclot)
            self.bloodclot.change_x = BLOODCLOT_SPEED
    
    def spawn_bonus(self, delta_time) -> None:
        self.time_since_last_bonus += delta_time
        if self.time_since_last_bonus >= self.bonus_spawning_freq:
            self.time_since_last_bonus = 0.0

            self.bonus = bn.Bonus(self.bonus_texture)
            self.bonus.position = (
                random.randint(
                    int(self.bonus.width), int(WINDOW_WIDTH - self.bonus.width)
                ),
                random.randint(
                    int(self.bonus.height), int(WINDOW_HEIGHT - self.bonus.height)
                ),
            )
            self.bonus.growth_factor = random.uniform(
                BLOODCLOT_SCALE_MIN, BLOODCLOT_SCALE_MAX
            )
            self.bonus_list.append(self.bonus)
            self.bonus.change_x = BLOODCLOT_SPEED

    def check_player_collisions(self):
        virus_hit_player_list = arcade.check_for_collision_with_list(
            self.player, self.virus_list
        )
        for virus in virus_hit_player_list:
            self.player.lives -= 1
            virus.remove_from_sprite_lists()

        bloodclot_hit_player_list = arcade.check_for_collision_with_list(
            self.player, self.bloodclot_list
        )
        for bloodclot in bloodclot_hit_player_list:
            if not bloodclot.killed_player:
                bloodclot.killed_player = True
                self.player.lives -= 1
                
        player_hit_bonus_list = arcade.check_for_collision_with_list(
            self.player, self.bonus_list
        )
        for bonus in player_hit_bonus_list:
            bonus.remove_from_sprite_lists()
            self.player.score += 1000

    def check_bullet_collisions(self):
        for bullet in self.bullet_list:
            bullet_hit_virus_list = arcade.check_for_collision_with_list(
                bullet, self.virus_list
            )

            bullet_hit_bloodclot_list = arcade.check_for_collision_with_list(
                bullet, self.bloodclot_list
            )

            for bloodclot in bullet_hit_bloodclot_list:
                if not bloodclot.hit:
                    bloodclot.hit = True
                    bloodclot.growth_factor = random.uniform(
                        BLOODCLOT_SCALE_MIN, BLOODCLOT_SCALE_MAX
                    )
                bullet.remove_from_sprite_lists()

            for virus in bullet_hit_virus_list:
                virus.remove_from_sprite_lists()
                bullet.remove_from_sprite_lists()
                self.player.score += HIT_VALUE * self.player.multiplier


def main() -> None:
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.center_window()
    game = GameView()
    game.setup()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
