# This class represents a player with a position, a path and an old position
class Player:
    def __init__(self, position: (int, int), score, old_position: []):
        self.position = position
        self.score = score
        if not old_position:    # If old position is NULL, then we initialize it with the starting position
            self.old_position = [position]
        else:
            self.old_position = old_position
