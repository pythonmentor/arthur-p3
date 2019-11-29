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

        # initialise basic labyrinth
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
                else:
                    Labyrinth.maps[key] = Square(coords)
                    Square.add_square(key)

        # place itams
        items = [
            {'name': 'Item 1'},
            {'name': 'Item 2'},
            {'name': 'Item 3'},
            {'name': 'Item 4'},
        ]
        for item in items:
            key = Square.random_pop_square()
            coords = {'x': key[0], 'y': key[1]}
            name = item['name']
            Labyrinth.maps[key] = Item(coords, name)

        Square.squares = None


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
