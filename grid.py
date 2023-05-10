from player import Player
from collections import deque


# This class represents the logical grid that we can process as a matrix
class Grid:
    def __init__(self, grid: [[str]]):
        # Grid parameters
        self.matrix = grid     # Logical grid
        self.length = len(self.matrix)  # Number of rows
        self.width = len(self.matrix[0])  # Number of columns

        # Game parameters
        self.end_score = float("inf")  # For now, the best path is +inf, to be sure to find a lower one
        self.end_game = False
        self.player = Player(self.find_starting_position(), 0, [])  # Starting player

        # Array that represents all the positions that we will process
        self.waiting_positions = deque([self.player])

    # This method finds the starting position in the logical grid thanks to the letter "S"
    def find_starting_position(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.matrix[i][j] == "S":    # If we find the starting position
                    return i, j

    # This method processes each time step during the analysis of the grid
    def next_time_step(self):
        if not self.waiting_positions:
            self.end_game = True
        else:
            for _ in range(len(self.waiting_positions)):  # For all the position of the player that we want to process
                player = self.waiting_positions.popleft()
                i, j = player.position
                if self.matrix[i][j] == 'G':    # If the player arrives to the ending positions
                    self.end_score = player.score    # End of the path, but we continue to search for the shortest path
                else:
                    self.move((i + 1, j), player)  # try to move up
                    self.move((i - 1, j), player)  # try to move down
                    self.move((i, j + 1), player)  # try to move right
                    self.move((i, j - 1), player)  # try to move left

    # This method can create a new player with a specific change of position that allow the player to move
    def move(self, move: (int, int), player: Player):
        # If the new position is valid (no wall/overflow) and not already processed in this path
        if self.valid_location(move) and (move not in player.old_position):
            if self.matrix[move[0]][move[1]] == 'G':
                val = 0
            else:
                val = int(self.matrix[move[0]][move[1]])
            old_position = player.old_position.copy()
            old_position.append(move)
            new_player = Player(move, player.score + val, old_position)
            if new_player.score < self.end_score:
                self.waiting_positions.append(new_player)

    # This method checks the position passed in argument on the grid,
    # Avoiding an index error or the presence of a wall
    def valid_location(self, move: (int, int)):
        i = move[0]
        j = move[1]
        if not (0 <= i < self.length) or not (0 <= j < self.width):  # Checks index
            return False
        if self.matrix[i][j] == 'X':  # Checks presence of a wall
            return False
        return True  # The position is valid, return True

    # This function displays the grid on the screen, useful when developing the project.
    def display_grid(self):
        for line in self.matrix:
            for car in line:
                print(car, end='')
            print('')
        print("\n\n")