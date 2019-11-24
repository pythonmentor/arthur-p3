class Gyver(object):
    """docstring for Gyver."""

    # -tc- Attention, en python, ça déclare des
    # -tc- attributs de classe, pas d'instance.
    coords = []
    deck = 0
    life = -1

    def __init__(self, coords, **kwargs):
        # -tc- Inutile ici, mais la syntaxe correcte est super().__init__()
        super(Gyver, self).__init__()
        self.coords = coords
        self.deck = 1
        self.life = 100
