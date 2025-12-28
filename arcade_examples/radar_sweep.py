import math

import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Radar Sweep Example"

CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
RADIANS_PER_FRAME = 0.02
SWEEP_LENGTH = 250


class Radar:
    def __init__(self):
        self.angle = 0.0

    def update(self, delta_time=0):
        self.angle += RADIANS_PER_FRAME * delta_time

    def draw(self):
        x = SWEEP_LENGTH * math.sin(self.angle) + CENTER_X
        y = SWEEP_LENGTH * math.cos(self.angle) + CENTER_Y

        arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 4)

        arcade.draw_circle_outline(
            CENTER_X,
            CENTER_Y,
            SWEEP_LENGTH,
            arcade.color.DARK_GREEN,
            10,
            num_segments=60,
        )


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.radar = Radar()
        self.background_color = arcade.color.BLACK
        self.speed = 60
        self.speed_keys = {'up': False, 'down': False}

    def on_update(self, delta_time):
        if self.speed_keys['up'] and self.speed <= 1500:
            self.speed += 10
        if self.speed_keys['down'] and self.speed > 10:
            self.speed -= 10
            
        self.radar.update(int(delta_time * self.speed))

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.speed_keys['up'] = True
        if symbol == arcade.key.DOWN:
            self.speed_keys['down'] = True
                
    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP:
            self.speed_keys['up'] = False
        if symbol == arcade.key.DOWN:
            self.speed_keys['down'] = False
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.speed > 0:
                self.temp_speed = self.speed
                self.speed = 0
            else:
                self.speed = self.temp_speed
        
    def on_draw(self):
        self.clear()
        self.radar.draw()
        arcade.draw_text(
            f"Sweep speed: {self.speed}", 10, WINDOW_HEIGHT - 30, arcade.color.WHITE, 20
        )


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    game = GameView()

    window.show_view(game)

    arcade.run()


if __name__ == "__main__":
    main()
