class Square():
    """
        A Square is an Area where Mac Gyver can move or not.
    """

    coords = []
    type = 'Floor'

    def __init__(self, coords):
        self.coords = coords

    def can_move(self):
        """
            True if Mac Gyver can move on it. False is he can't.
        """
        return True

    def after_move(self, gyver):
        """
            Execute method(s) after a move
        """
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
