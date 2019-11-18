from squares import *

class Labyrinth(object):
    """docstring for Labyrinth."""

    maps = []

    def __init__(self, **kwargs):
        super(Labyrinth, self).__init__()
        self.buildLabyrinth()

    def buildLabyrinth(self):
        laby = [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'p', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', 'g', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ]

        for iRow in range(len(laby)):
            row = laby[iRow]
            mapRow = []
            for iColumn in range(len(row)):
                square = row[iColumn]
                coords = [iRow, iColumn]

                if(square == 'w'):
                    mapRow.append(Wall(coords))
                elif(square == 'g'):
                    mapRow.append(Guard(coords))
                else:
                    mapRow.append(Square(coords))

                print('Square Loaded : ' + str(square))

            self.maps.append(mapRow)
