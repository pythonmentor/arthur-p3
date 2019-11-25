from squares import Square, Wall, Guard

class Labyrinth():
    """docstring for Labyrinth."""

    maps = []

    def __init__(self, **kwargs):
        self.build_labyrinth()

    def build_labyrinth(self):
        laby = [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', '_', '_', 'w', '_', '_', '_', 'w', 'g', 'w'],
            ['w', 'w', '_', 'w', '_', 'w', '_', 'w', '_', 'w'],
            ['w', '_', '_', '_', '_', 'w', 'w', 'w', '_', 'w'],
            ['w', '_', 'w', 'w', 'w', '_', '_', '_', '_', 'w'],
            ['w', '_', 'w', '_', '_', 'w', '_', 'w', 'w', 'w'],
            ['w', '_', 'w', '_', 'w', '_', '_', '_', '_', 'w'],
            ['w', '_', 'w', '_', 'w', 'w', 'w', 'w', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ]

        for i_row, row in enumerate(laby):
            map_row = []
            for i_column, square in enumerate(row):
                coords = [i_row, i_column]

                if(square == 'w'):
                    map_row.append(Wall(coords))
                elif(square == 'g'):
                    map_row.append(Guard(coords))
                else:
                    map_row.append(Square(coords))

            self.maps.append(map_row)
