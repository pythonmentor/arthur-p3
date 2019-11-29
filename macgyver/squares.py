class Square:
    """
        A Square is an Area where Mac Gyver can move or not.
    """

    def __init__(self, coords):
        """
            coords = {'x': <int>, 'y': <int>}
        """
        self.coords = coords
        self.type = 'Floor'

    def can_move(self):
        """
            True if Mac Gyver can move on it. False is he can't.
        """
        return True

    def after_move(self, **kwargs):
        """
            Execute method(s) after a move
        """
        return 0

    def get_type(self):
        return self.type

class Wall(Square):
    """docstring for Wall."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Wall"

    def can_move(self):
        return False


class Item(Square):
    """docstring for Item."""

    def __init__(self, coords, name):
        super().__init__(coords)
        self.type = name
        self.taken = False

    def after_move(self, **kwargs):
        gyver = kwargs.pop('gyver', None)
        if(gyver != None):
            gyver.add_item(self.type)
            self.taken = True

    def get_type(self):
        return 'Floor' if self.taken else self.type


class Guard(Square):
    """docstring for Guard."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Guard"

    def after_move(self, **kwargs):
        gyver = kwargs.pop('gyver', None)
        if(gyver != None):
            gyver.set_win()
