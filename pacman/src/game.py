import time
from pacman.src.maze import create_default_maze
from pacman.src.pacman import Pacman
from pacman.src.ghost import Ghost
from pacman.src.settings import (
    PACMAN_CHAR, COLOR_PAIR_PACMAN, DOT_CHAR, POWER_PELLET_CHAR,
    DOT_SCORE, POWER_PELLET_SCORE, EMPTY_CHAR, COLOR_PAIR_GHOST,
    STARTING_LIVES, PACMAN_START_POS, GHOST_START_POS,
    FRIGHTENED_DURATION, GHOST_EATEN_SCORE
)

class Game:
    """
    Manages the main game logic, including the game loop, state, rules,
    and rendering.
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen.stdscr.nodelay(True)
        self.maze = create_default_maze()
        self.pacman = Pacman(PACMAN_START_POS[0], PACMAN_START_POS[1])
        self.ghosts = [Ghost(pos[0], pos[1], COLOR_PAIR_GHOST) for pos in GHOST_START_POS]
        self.score = 0
        self.lives = STARTING_LIVES
        self.frightened_timer = 0
        self.is_running = False
        self.game_over_message = ""
        self.total_dots = self.count_dots()
        self.animation_counter = 0

    def count_dots(self):
        """Counts the initial number of dots and power pellets in the maze."""
        count = 0
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                char = self.maze.get_char(x, y)
                if char == DOT_CHAR or char == POWER_PELLET_CHAR:
                    count += 1
        return count

    def run(self):
        """Starts and runs the main game loop."""
        self.is_running = True
        while self.is_running:
            self.process_input()
            self.update_state()
            self.render()
            time.sleep(0.15)
        self.show_game_over()

    def process_input(self):
        """Handles user input."""
        key = self.screen.get_input()
        if key != -1:
            if key in [Pacman.UP, Pacman.DOWN, Pacman.LEFT, Pacman.RIGHT]:
                self.pacman.move(key, self.maze)
            elif key == ord('q'):
                self.is_running = False

    def update_state(self):
        """Updates the game state."""
        self.animation_counter += 1
        self.pacman.update_animation(self.animation_counter)
        self.handle_dot_eating()
        self.update_ghosts()
        self.check_collisions()

    def handle_dot_eating(self):
        """Handles Pac-Man eating dots and power pellets."""
        char = self.maze.get_char(self.pacman.x, self.pacman.y)
        if char == DOT_CHAR:
            self.score += DOT_SCORE
            self.maze.set_char(self.pacman.x, self.pacman.y, EMPTY_CHAR)
            self.total_dots -= 1
        elif char == POWER_PELLET_CHAR:
            self.score += POWER_PELLET_SCORE
            self.maze.set_char(self.pacman.x, self.pacman.y, EMPTY_CHAR)
            self.total_dots -= 1
            self.frighten_ghosts()

        if self.total_dots == 0:
            self.game_over_message = "YOU WIN!"
            self.is_running = False

    def update_ghosts(self):
        """Updates the state and position of all ghosts."""
        if self.frightened_timer > 0:
            self.frightened_timer -= 1
            if self.frightened_timer == 0:
                for ghost in self.ghosts:
                    ghost.state = 'chase'

        for ghost in self.ghosts:
            ghost.move(self.maze)

    def frighten_ghosts(self):
        """Puts all ghosts into the 'frightened' state."""
        self.frightened_timer = FRIGHTENED_DURATION
        for ghost in self.ghosts:
            ghost.state = 'frightened'

    def check_collisions(self):
        """Checks for collisions between Pac-Man and ghosts."""
        for ghost in self.ghosts:
            if self.pacman.x == ghost.x and self.pacman.y == ghost.y:
                if ghost.state == 'frightened':
                    self.score += GHOST_EATEN_SCORE
                    ghost.reset_position()
                else: # 'chase' state
                    self.handle_pacman_death()

    def handle_pacman_death(self):
        """Handles the event of Pac-Man losing a life."""
        self.lives -= 1
        if self.lives > 0:
            time.sleep(1)
            self.reset_positions()
        else:
            self.game_over_message = "GAME OVER"
            self.is_running = False

    def reset_positions(self):
        """Resets Pac-Man and ghosts to their starting positions."""
        self.pacman.x, self.pacman.y = PACMAN_START_POS
        for ghost in self.ghosts:
            ghost.reset_position()

    def render(self):
        """Renders the current game state, including animations."""
        self.screen.clear()
        status_text = f"Score: {self.score}  Lives: {self.lives}"
        self.screen.draw(0, 0, status_text)

        # Make power pellets blink
        hide_pellet = self.animation_counter % 10 < 5
        self.screen.draw_maze(
            self.maze, y_offset=1,
            hide_char=POWER_PELLET_CHAR if hide_pellet else None
        )

        self.screen.draw(
            self.pacman.x, self.pacman.y + 1, self.pacman.char, COLOR_PAIR_PACMAN
        )

        for ghost in self.ghosts:
            # Make frightened ghosts blink when the timer is low
            if ghost.state == 'frightened' and self.frightened_timer < 20:
                if self.animation_counter % 4 < 2:
                    continue # Skip drawing this frame to make it blink
            self.screen.draw(ghost.x, ghost.y + 1, ghost.char, ghost.color)

        self.screen.refresh()

    def show_game_over(self):
        """Displays the final game over message."""
        if self.game_over_message:
            self.screen.clear()
            h, w = self.screen.stdscr.getmaxyx()
            x = w // 2 - len(self.game_over_message) // 2
            y = h // 2
            self.screen.draw(x, y, self.game_over_message)
            self.screen.refresh()
            time.sleep(3)
