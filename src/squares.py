class Square(object):
    """docstring for Square."""

    coords = []
    type = 'Floor'

    def __init__(self, coords):
        self.coords = coords

    # -tc- can_move
    def canMove(self):
        return False

    # -tc- que fait after_move
    def afterMove(self, gyver):
        return 0

class Wall(Square):
    """docstring for Wall."""

    def __init__(self, coords):
        # -tc- super().__init__(coords)
        super(Wall, self).__init__(coords)
        self.type = "Wall"

class Guard(Square):
    """docstring for Guard."""

    def __init__(self, coords):
        # -tc- super().__init__(coords)
        super(Guard, self).__init__(coords)
        self.type = "Guard"

    # -tc- Dans Square, after_move retourne une valeur
    def afterMove(self, gyver):
        gyver.win()
