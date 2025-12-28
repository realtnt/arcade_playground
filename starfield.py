import random

import arcade

from constants import * # noqa: F403

BG_STAR_COLORS = (255, 255, 255, 95)
FG_STAR_COLORS = [
    arcade.color.WHITE,
    arcade.color.BABY_BLUE,
    arcade.color.AQUA,
    arcade.color.BUFF,
    arcade.color.ALIZARIN_CRIMSON,
]


class Starfield:
    def __init__(self):
        super().__init__()

        self.fg_star_speed = 100
        self.bg_star_speed = 60
        self.fg_stars1 = arcade.shape_list.ShapeElementList()
        self.create_starfield(self.fg_stars1, random_color=True)
        self.fg_stars2 = arcade.shape_list.ShapeElementList()
        self.fg_stars2.center_x = WINDOW_WIDTH
        self.create_starfield(self.fg_stars2, random_color=True)
        self.bg_stars1 = arcade.shape_list.ShapeElementList()
        self.create_starfield(self.bg_stars1)
        self.bg_stars2 = arcade.shape_list.ShapeElementList()
        self.bg_stars2.center_x = WINDOW_WIDTH
        self.create_starfield(self.bg_stars2)

    def draw(self) -> None:
        self.fg_stars1.draw()
        self.fg_stars2.draw()
        self.bg_stars1.draw()
        self.bg_stars2.draw()

    def update(self, delta_time):
        self.fg_stars1.center_x -= self.fg_star_speed * delta_time
        self.fg_stars2.center_x -= self.fg_star_speed * delta_time
        if self.fg_stars1.center_x < -WINDOW_WIDTH:
            self.fg_stars1.center_x = WINDOW_WIDTH
        if self.fg_stars2.center_x < -WINDOW_WIDTH:
            self.fg_stars2.center_x = WINDOW_WIDTH

        self.bg_stars1.center_x -= self.bg_star_speed * delta_time
        self.bg_stars2.center_x -= self.bg_star_speed * delta_time
        if self.bg_stars1.center_x < -WINDOW_WIDTH:
            self.bg_stars1.center_x = WINDOW_WIDTH
        if self.bg_stars2.center_x < -WINDOW_WIDTH:
            self.bg_stars2.center_x = WINDOW_WIDTH

    def create_starfield(
        self,
        batch: arcade.shape_list.ShapeElementList,
        color=BG_STAR_COLORS,
        random_color=False,
    ):
        for i in range(200):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            w = random.randint(1, 3)
            h = random.randint(1, 3)
            if random_color:
                color = random.choice(FG_STAR_COLORS)
            star = arcade.shape_list.create_rectangle_filled(x, y, w, h, color)
            batch.append(star)
