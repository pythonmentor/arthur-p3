from .squares import Square, Wall, Guard, Item

class Labyrinth:
    """Static Labyrinth."""

    maps = {}
    rows = 0
    columns = 0

    def build_labyrinth():
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

        Labyrinth.rows = len(laby)
        Labyrinth.columns = len(laby[0])

        for i_row, row in enumerate(laby):
            for i_column, square in enumerate(row):
                x = i_column
                y = i_row
                key = (x, y)
                coords = {'x': x, 'y': y}

                if(square == 'w'):
                    Labyrinth.maps[key] = Wall(coords)
                elif(square == 'g'):
                    Labyrinth.maps[key] = Guard(coords)
                elif(square == '1'):
                    Labyrinth.maps[key] = Item(coords, 'Item 1')
                elif(square == '2'):
                    Labyrinth.maps[key] = Item(coords, 'Item 2')
                elif(square == '3'):
                    Labyrinth.maps[key] = Item(coords, 'Item 3')
                elif(square == '4'):
                    Labyrinth.maps[key] = Item(coords, 'Item 4')
                else:
                    Labyrinth.maps[key] = Square(coords)


    def get_square(coords):
        key = (coords['x'], coords['y'])
        return Labyrinth.maps[key]


    def can_move(coords):
        square = Labyrinth.get_square(coords)
        if(square != None):
            can_move = square.can_move()
        else:
            return False

        return can_move
