from .labyrinth import Labyrinth
from .gyver import Gyver

class Driver:
    """
        **Interface**
        The driver manage the interface, if the game run with the terminal or
        with pygame.
    """

    def draw_labyrinth(self):
        """
            Function to draw the labyrinth with MacGyver.
        """

        print('This is an interface')

    def wait_for_move(self):
        """
            Function to wait next move. Return String who know the move.
        """

        print('This is an interface')
        return None

    def win_scenario(self):
        """
            What the program do when MacGyver win.
        """

        print('This is an interface')

    def lose_scenario(self):
        """
            What the program do when MacGyver lose.
        """

        print('This is an interface')


class TerminalDriver(Driver):
    """
        Terminal Driver. Print the labyrinth and ask for input (L, R, U, D).
        Win and Lose scénarios print respectively
        'Well Done !' and 'Game Over...'
    """

    def draw_labyrinth(self):
        print('\n')

        maps = Labyrinth.maps

        print('##########')

        items_string = 'Items : '
        if(len(Gyver.items) == 0):
            items_string += '---'
        for name, taken in Gyver.items.items():
            if(taken):
                items_string += ' [' + name + '] '
        print(items_string)
        print('##########\n')

        for i_row in range(Labyrinth.rows):
            laby_string = ''
            for i_column in range(Labyrinth.columns):
                square = maps[(i_column, i_row)]
                if(Gyver.coords == square.coords):
                    laby_string += '\t' + 'Gyver'
                else:
                    laby_string += '\t' +  square.get_type()

            print(laby_string)


    def wait_for_move(self):
        return input('L, R, U, D (or QUIT) :\n')


    def win_scenario(self):
        print('Well Done !')

    def lose_scenario(self):
        print('Game Over...')
