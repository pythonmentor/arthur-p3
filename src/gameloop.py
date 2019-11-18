class GameLoop(object):
    """docstring for GameLoop."""

    gyver = None
    labyrinth = None

    def __init__(self, gyver, labyrinth, **kwargs):
        super(GameLoop, self).__init__()
        self.gyver = gyver
        self.labyrinth = labyrinth

        self.printGame()

    def printGame(self):
        maps = self.labyrinth.maps

        for row in maps:
            s = ''
            for square in row:
                if(self.gyver.coords == square.coords):
                    s += '\t' + 'Gyver'
                else:
                    s += '\t' +  square.type

            print(s)
