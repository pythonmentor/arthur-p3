class Square():
    """docstring for Square."""

    coords = []
    type = 'Floor'

    def __init__(self, coords):
        self.coords = coords

    def can_move(self):
        return True

    def after_move(self, gyver):
        return 0

class Wall(Square):
    """docstring for Wall."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Wall"

    def can_move(self):
        return False

class Guard(Square):
    """docstring for Guard."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Guard"

    def after_move(self, gyver):
        gyver.win()
