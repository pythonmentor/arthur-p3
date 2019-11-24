class GameLoop(object):
    """docstring for GameLoop."""

    # -tc- inutile, pas utilisé
    gyver = None
    labyrinth = None

    def __init__(self, gyver, labyrinth, **kwargs):
        # -tc- inutile
        super(GameLoop, self).__init__()
        self.gyver = gyver
        self.labyrinth = labyrinth

        self.printGame()

    # -tc- attention aux conventions de nommage: voir PEP8
    def printGame(self):
        maps = self.labyrinth.maps

        # -tc- pour une meilleure visualisation en terminal, afficher une seule lettre par case
        for row in maps:
            s = ''
            for square in row:
                if(self.gyver.coords == square.coords):
                    s += '\t' + 'Gyver'
                else:
                    s += '\t' +  square.type

            print(s)
