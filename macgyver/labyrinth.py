import os

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

    def build_labyrinth():
        gyver_coords = (1, 1)

        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        laby_file = open(os.path.join(ROOT_DIR, 'laby.txt'))

        laby = []

        for line in laby_file:
            row = []
            for s in line:
                if(s != '\n'):
                    row.append(s)
            laby.append(row)

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
                elif(square == 'p'):
                    Labyrinth.maps[coords] = Square(coords)
                    gyver_coords = coords
                else:
                    Labyrinth.maps[coords] = Square(coords)
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

        return gyver_coords


    def get_square(coords):
        return Labyrinth.maps[coords]


    def can_move(coords):
        square = Labyrinth.get_square(coords)
        if(square != None):
            can_move = square.can_move()
        else:
            return False

        return can_move
