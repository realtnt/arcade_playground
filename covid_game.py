import arcade

import random

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Covid19"

bg_star_color = (255, 255, 255, 95)
fg_star_colors = [arcade.color.WHITE, arcade.color.BABY_BLUE, arcade.color.AQUA, arcade.color.BUFF, arcade.color.ALIZARIN_CRIMSON]

def create_starfield(batch: arcade.shape_list.ShapeElementList, color=bg_star_color, random_color=False):
    for i in range(200):
        x = random.randint(0, 1280)
        y = random.randint(0, 720)
        w = random.randint(1, 3)
        h = random.randint(1, 3)
        if random_color:
            color = random.choice(fg_star_colors)
        star = arcade.shape_list.create_rectangle_filled(x, y, w, h, color)
        batch.append(star)

class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.fg_star_speed = 100
        self.bg_star_speed = 60
        
        self.fg_stars1 = arcade.shape_list.ShapeElementList()
        create_starfield(self.fg_stars1, random_color=True)
        
        self.fg_stars2 = arcade.shape_list.ShapeElementList()
        self.fg_stars2.center_x = WINDOW_WIDTH
        create_starfield(self.fg_stars2, random_color=True)
        
        self.bg_stars1 = arcade.shape_list.ShapeElementList()
        create_starfield(self.bg_stars1)
        
        self.bg_stars2 = arcade.shape_list.ShapeElementList()
        self.bg_stars2.center_x = WINDOW_WIDTH
        create_starfield(self.bg_stars2)
        
        
        
        
    def on_draw(self) -> None:
        self.clear()
        
        self.fg_stars1.draw()
        self.fg_stars2.draw()
        self.bg_stars1.draw()
        self.bg_stars2.draw()
        
    def on_update(self, delta_time) -> None:
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
        
    
     
def main() -> None:      
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE) 
    window.center_window()
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
