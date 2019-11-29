import os
import pygame

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


class PygameDriver(Driver):
    """
        Pygame Driver. Draw the labyrinth with MacGyver and wait an event.
    """

    def __init__(self, fps):
        """
            fps : frame per second (int)
        """
        super().__init__()
        pygame.init()
        pygame.time.delay(int(1000/fps))

        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Mac Gyver Evasion')
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        #self._load_images()

    def _load_images(self):
        """
            private method : load images from the ressources
            (wall, guard, etc...)
        """
        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.wall_img = pygame.image.load(os.path.join(ROOT_DIR,'res/laby/wall.png'))
        self.guard_img = pygame.image.load(os.path.join(ROOT_DIR,'res/laby/guard.png'))
        self.gyver_img = pygame.image.load(os.path.join(ROOT_DIR,'res/laby/gyver.png'))

    def _draw_laby(self):
        """
            private method : draw the laby with items and the guard
        """
        return 0

    def _draw_gyver(self):
        """
            private method : draw gyver and add the numbers of items he hold
        """
        return 0

    def draw_labyrinth(self):
        self._draw_laby()
        self._draw_gyver()

    def wait_for_move(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return 'QUIT'

            elif(event.type == pygame.KEYDOWN):
                keys = pygame.key.get_pressed()

                if(keys[pygame.K_UP]):
                    return 'U'
                elif(keys[pygame.K_DOWN]):
                    return 'D'
                elif(keys[pygame.K_RIGHT]):
                    return 'R'
                elif(keys[pygame.K_LEFT]):
                    return 'L'

        return 0


    def win_scenario(self):
        print('Well Done !')

    def lose_scenario(self):
        print('Game Over...')
