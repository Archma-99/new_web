import curses
from pacman.src.screen import Screen
from pacman.src.game import Game

def main(stdscr):
    """
    The main function to run the Pac-Man game.
    This function initializes the screen and game, then starts the game loop.
    """
    curses.curs_set(0)  # Hide the cursor
    screen = Screen(stdscr)
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    curses.wrapper(main)
