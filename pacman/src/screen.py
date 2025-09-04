import curses
from pacman.src.settings import (
    COLOR_PAIR_WALL, COLOR_PAIR_DOT, COLOR_PAIR_POWER_PELLET, COLOR_PAIR_PACMAN, COLOR_PAIR_GHOST, COLOR_PAIR_DEFAULT,
    COLOR_PAIR_FRIGHTENED_GHOST, WALL_CHAR, DOT_CHAR, POWER_PELLET_CHAR
)

class Screen:
    """
    Manages the terminal screen using the curses library.
    This class is responsible for initializing colors and drawing the game state.
    """
    def __init__(self, stdscr):
        """
        Initializes the Screen with a curses window object.
        """
        self.stdscr = stdscr
        self.stdscr.keypad(True)
        self.init_colors()

    def init_colors(self):
        """Initializes color pairs used in the game."""
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(COLOR_PAIR_WALL, curses.COLOR_BLUE, -1)
        curses.init_pair(COLOR_PAIR_DOT, curses.COLOR_WHITE, -1)
        curses.init_pair(COLOR_PAIR_POWER_PELLET, curses.COLOR_YELLOW, -1)
        curses.init_pair(COLOR_PAIR_PACMAN, curses.COLOR_YELLOW, -1)
        curses.init_pair(COLOR_PAIR_GHOST, curses.COLOR_RED, -1)
        curses.init_pair(COLOR_PAIR_FRIGHTENED_GHOST, curses.COLOR_CYAN, -1)
        curses.init_pair(COLOR_PAIR_DEFAULT, curses.COLOR_WHITE, -1)

    def get_color_pair(self, char):
        """Returns the color pair ID for a given maze character."""
        if char == WALL_CHAR:
            return COLOR_PAIR_WALL
        elif char == DOT_CHAR:
            return COLOR_PAIR_DOT
        elif char == POWER_PELLET_CHAR:
            return COLOR_PAIR_POWER_PELLET
        else:
            return COLOR_PAIR_DEFAULT

    def draw_maze(self, maze, y_offset=0, hide_char=None):
        """
        Draws the entire maze on the screen at a given y-offset.
        Optionally hides a specific character type (e.g., for blinking).
        """
        for y in range(maze.height):
            for x in range(maze.width):
                char = maze.get_char(x, y)
                if char == hide_char:
                    char = ' ' # Render as empty space
                color_pair = self.get_color_pair(char)
                self.stdscr.addstr(y + y_offset, x, char, curses.color_pair(color_pair))

    def draw(self, x, y, text, color_pair_id=COLOR_PAIR_DEFAULT):
        """Draws a string of text at a given position with a given color."""
        color = curses.color_pair(color_pair_id)
        self.stdscr.addstr(y, x, text, color)

    def get_input(self):
        """Gets a single character of input from the user."""
        return self.stdscr.getch()

    def refresh(self):
        """Refreshes the screen to show any changes."""
        self.stdscr.refresh()

    def clear(self):
        """Clears the entire screen."""
        self.stdscr.clear()
