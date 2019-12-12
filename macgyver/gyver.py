from .labyrinth import Labyrinth


class Gyver:
    """Full Static Object, here we move the player with move() function.

    Before using this class, we need to initialise it with init_gyver.
    """

    win = False
    lose = False

    coords = None
    items = {}

    def init_gyver(gyver_coords):
        """
            coords = (x, y)
        """
        Gyver.coords = gyver_coords

    def move(**kwargs):
        """You can move the player with the simple method
        move(x=<int:optional>, y=<int:optional>).

        This method verify if gyver can move in the labyrinth and return
        the current square.
        """
        x = kwargs.pop('x', 0)
        y = kwargs.pop('y', 0)

        coords = (Gyver.coords[0]+x, Gyver.coords[1]+y)

        if(Labyrinth.can_move(coords)):
            Gyver.coords = coords

        return Labyrinth.get_square(Gyver.coords)

    def set_win(self):
        Gyver.win = True

    def set_lose(self):
        Gyver.lose = True

    def add_item(self, name):
        Gyver.items[name] = True
