from .squares import Square, Wall, Guard, Item

class Labyrinth:
    """
        Full Static Object. Need to call build_labyrinth before use. The class
        can be used to know quickely if MacGyver can move in a square or to
        get a square by coords.
    """

    maps = {}
    rows = 0
    columns = 0

    def build_labyrinth(gyver_coords):
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
                coords = (x, y)

                if(square == 'w'):
                    Labyrinth.maps[coords] = Wall(coords)
                elif(square == 'g'):
                    Labyrinth.maps[coords] = Guard(coords)
                else:
                    Labyrinth.maps[coords] = Square(coords)
                    if(gyver_coords != coords):
                        Square.add_square(coords)

        # place itams
        items = [
            {'name': 'Item 1'},
            {'name': 'Item 2'},
            {'name': 'Item 3'},
            {'name': 'Item 4'},
        ]
        for item in items:
            coords = Square.random_pop_square()
            name = item['name']
            Labyrinth.maps[coords] = Item(coords, name)

        Square.squares = None


    def get_square(coords):
        return Labyrinth.maps[coords]


    def can_move(coords):
        square = Labyrinth.get_square(coords)
        if(square != None):
            can_move = square.can_move()
        else:
            return False

        return can_move
