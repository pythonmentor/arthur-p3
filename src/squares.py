class Square(object):
    """docstring for Square."""

    coords = []
    type = 'Floor'

    def __init__(self, coords):
        self.coords = coords

    def canMove(self):
        return False

    def afterMove(self, gyver):
        return 0

class Wall(Square):
    """docstring for Wall."""

    def __init__(self, coords):
        super(Wall, self).__init__(coords)
        self.type = "Wall"

class Guard(Square):
    """docstring for Guard."""

    def __init__(self, coords):
        super(Guard, self).__init__(coords)
        self.type = "Guard"

    def afterMove(self, gyver):
        gyver.win()
