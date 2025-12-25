from telnetlib import WILL

import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Arcade Playground"


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.background_color = arcade.color.AMAZON

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self) -> None:
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        ...

    def on_draw(self) -> None:
        """Render the screen."""

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time) -> None:
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        ...

    def on_key_press(self, key, key_modifiers) -> None:
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        ...

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        """
        Called whenever the user lets off a previously pressed key.
        """
        ...

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        ...

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        ...

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        ...

def main():
    """ Main function """
    # Create a window object. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    
    # Create and setup the GameView
    game = GameView()
    
    # Show GameView on screen
    window.show_view(game)
    
    # Start the arcade game loop
    arcade.run()
    
if __name__ == "__main__":
    main()
