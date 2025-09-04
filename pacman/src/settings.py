# Game Settings
# This file stores constants and configuration settings for the game.

# Screen dimensions (will be derived from the maze)
# Note: The classic Pac-Man maze is 28x36 characters.

# Game element characters
WALL_CHAR = '#'
DOT_CHAR = '.'
POWER_PELLET_CHAR = 'o'
PACMAN_CHAR = 'C'
GHOST_CHAR = 'G'
EMPTY_CHAR = ' '

# Colors (curses color pairs)
# These are just IDs. The actual colors will be defined in the Screen class.
COLOR_PAIR_WALL = 1
COLOR_PAIR_DOT = 2
COLOR_PAIR_POWER_PELLET = 3
COLOR_PAIR_PACMAN = 4
COLOR_PAIR_GHOST = 5
COLOR_PAIR_DEFAULT = 6

# Scoring
DOT_SCORE = 10
POWER_PELLET_SCORE = 50

# Game Rules
STARTING_LIVES = 3
PACMAN_START_POS = (13, 23)
GHOST_START_POS = [(13, 14)] # A list for multiple ghosts
FRIGHTENED_DURATION = 50 # in frames/game loops
GHOST_EATEN_SCORE = 200

# More Colors
COLOR_PAIR_FRIGHTENED_GHOST = 7
