import random
import curses
from pacman.src.settings import (
    GHOST_CHAR, WALL_CHAR, COLOR_PAIR_FRIGHTENED_GHOST
)

class Ghost:
    """
    Represents a ghost character, handling its movement, state, and AI.
    """
    def __init__(self, x, y, chase_color):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.char = GHOST_CHAR
        self.chase_color = chase_color
        self.frightened_color = COLOR_PAIR_FRIGHTENED_GHOST
        self.state = 'chase'  # Can be 'chase', 'frightened', or 'eaten'
        self.direction = random.choice([curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT])

    @property
    def color(self):
        """Returns the current color of the ghost based on its state."""
        if self.state == 'frightened':
            return self.frightened_color
        return self.chase_color

    def get_possible_moves(self, maze):
        """
        Returns a list of valid directions to move in (i.e., not into a wall).
        """
        possible_moves = []
        moves = {
            curses.KEY_UP: (0, -1),
            curses.KEY_DOWN: (0, 1),
            curses.KEY_LEFT: (-1, 0),
            curses.KEY_RIGHT: (1, 0),
        }
        for direction, (dx, dy) in moves.items():
            if maze.get_char(self.x + dx, self.y + dy) != WALL_CHAR:
                possible_moves.append(direction)
        return possible_moves

    def move(self, maze):
        """
        Moves the ghost based on its current AI state.
        """
        possible_moves = self.get_possible_moves(maze)
        reverse_directions = {
            curses.KEY_UP: curses.KEY_DOWN, curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT, curses.KEY_RIGHT: curses.KEY_LEFT,
        }
        reverse_direction = reverse_directions.get(self.direction)

        if len(possible_moves) > 1 and reverse_direction in possible_moves:
            possible_moves.remove(reverse_direction)

        if possible_moves:
            self.direction = random.choice(possible_moves)

        if self.direction == curses.KEY_UP: self.y -= 1
        elif self.direction == curses.KEY_DOWN: self.y += 1
        elif self.direction == curses.KEY_LEFT: self.x -= 1
        elif self.direction == curses.KEY_RIGHT: self.x += 1

    def reset_position(self):
        """Resets the ghost to its starting position."""
        self.x = self.start_x
        self.y = self.start_y
