import curses
from pacman.src.settings import WALL_CHAR

class Pacman:
    """
    Represents the Pac-Man player, handling its movement and state.
    """
    UP = curses.KEY_UP
    DOWN = curses.KEY_DOWN
    LEFT = curses.KEY_LEFT
    RIGHT = curses.KEY_RIGHT

    ANIMATION_FRAMES = {
        UP: ['v', 'V'],
        DOWN: ['^', 'V'],
        LEFT: ['>', 'O'],
        RIGHT: ['<', 'O'],
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = self.RIGHT
        self.char = self.ANIMATION_FRAMES[self.direction][0]

    def is_wall(self, x, y, maze):
        """Checks if the given coordinate is a wall in the maze."""
        return maze.get_char(x, y) == WALL_CHAR

    def update_animation(self, animation_counter):
        """Updates the character for the chomping animation."""
        frame = animation_counter % len(self.ANIMATION_FRAMES[self.direction])
        self.char = self.ANIMATION_FRAMES[self.direction][frame]

    def move(self, direction, maze):
        """
        Updates Pac-Man's position based on the chosen direction,
        if the path is not blocked by a wall.
        """
        next_x, next_y = self.x, self.y
        if direction == self.UP: next_y -= 1
        elif direction == self.DOWN: next_y += 1
        elif direction == self.LEFT: next_x -= 1
        elif direction == self.RIGHT: next_x += 1

        if not self.is_wall(next_x, next_y, maze):
            self.x = next_x
            self.y = next_y
            # Only change direction if the move was successful
            if self.direction != direction:
                 self.direction = direction
