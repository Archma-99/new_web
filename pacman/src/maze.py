from pacman.src.settings import EMPTY_CHAR

class Maze:
    """
    Represents the game maze, including its layout and properties.
    The layout is a list of strings, representing the grid.
    """
    def __init__(self, layout):
        self.layout = [list(row) for row in layout]
        self.height = len(self.layout)
        self.width = len(self.layout[0]) if self.height > 0 else 0

    def get_char(self, x, y):
        """
        Gets the character at a given coordinate in the maze.
        Returns None if the coordinates are out of bounds.
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.layout[y][x]
        return None

    def set_char(self, x, y, char):
        """
        Sets the character at a given coordinate in the maze.
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            self.layout[y][x] = char

# A classic Pac-Man maze design, simplified for a terminal.
# The 'G' characters are placeholders for ghost starting positions.
# The game logic will replace them with empty spaces.
DEFAULT_MAZE_LAYOUT = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "     #.##   GG   ##.#     ",
    "     #.## ######## ##.#     ",
    "######.## ######## ##.######",
    "      .   G  G   .      ",
    "######.## ######## ##.######",
    "     #.## ######## ##.#     ",
    "     #.##   GG   ##.#     ",
    "     #.##### ## #####.#     ",
    "######.##### ## #####.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

def create_default_maze():
    """
    Creates a default maze instance, replacing ghost placeholders with empty chars.
    """
    layout = [row.replace('G', EMPTY_CHAR) for row in DEFAULT_MAZE_LAYOUT]
    return Maze(layout)
