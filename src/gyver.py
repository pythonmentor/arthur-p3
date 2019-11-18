class Gyver(object):
    """docstring for Gyver."""

    coords = []
    deck = 0
    life = -1

    def __init__(self, coords, **kwargs):
        super(Gyver, self).__init__()
        self.coords = coords
        self.deck = 1
        self.life = 100
