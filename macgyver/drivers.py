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
        """Function to draw the labyrinth with MacGyver."""

        print('This is an interface')

    def wait_for_move(self):
        """Function to wait next move.

        Return String who know the move.
        """

        print('This is an interface')
        return None

    def win_scenario(self):
        """What the program do when MacGyver win."""

        print('This is an interface')

    def lose_scenario(self):
        """What the program do when MacGyver lose."""

        print('This is an interface')


class TerminalDriver(Driver):
    """Terminal Driver.

    Print the labyrinth and ask for input (L, R, U, D). Win and Lose
    scénarios print respectively 'Well Done !' and 'Game Over...'
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
                    laby_string += '\t' + square.get_type()

            print(laby_string)

    def wait_for_move(self):
        return input('L, R, U, D (or QUIT) :\n')

    def win_scenario(self):
        print('Well Done !')

    def lose_scenario(self):
        print('Game Over...')


class PygameDriver(Driver):
    """Pygame Driver.

    Draw the labyrinth with MacGyver and wait an event.
    """

    def __init__(self, fps):
        """
            fps : frame per second (int)
        """
        super().__init__()
        pygame.init()
        pygame.display.set_caption('Mac Gyver Evasion')
        pygame.time.delay(int(1000/fps))

        self.PIXEL = 50

        self._load_pygame()
        self._load_images()

    def _load_pygame(self):
        """
            private method : load pygame environment
        """

        self.screen = pygame.display.set_mode(
            (self.PIXEL*Labyrinth.columns+200, self.PIXEL*Labyrinth.rows)
        )

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((64, 0, 0))

        self.font_21 = pygame.font.SysFont('roboto', 21)
        self.font_21.set_bold(True)

        self.font_16 = pygame.font.SysFont('roboto', 16)

    def _load_images(self):
        """
            private method : load images from the ressources
            (wall, guard, etc...)
        """
        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.floor = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/floor.png'))
        self.wall = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/wall.png'))
        self.guard = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/guard.png'))
        self.gyver = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/gyver.png'))
        self.needle = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/needle.png'))
        self.plastic_tube = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/plastic_tube.png'))
        self.syringe = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/syringe.png'))
        self.ether = self._load_image(
            os.path.join(ROOT_DIR, 'res/laby/ether.png'))

    def _load_image(self, path):
        img = pygame.image.load(path)
        img = pygame.transform.scale(img, (50, 50))
        img.set_colorkey((255, 255, 255))

        return img

    def _draw_laby(self):
        """
            private method : draw the laby with items and the guard
        """

        self.screen.blit(self.background, (0, 0))

        for i_row in range(Labyrinth.rows):
            for i_column in range(Labyrinth.columns):
                coords = (i_column, i_row)
                pixel_coords = (self.PIXEL*i_column, self.PIXEL*i_row)

                square = Labyrinth.get_square(coords)
                if(square.get_type() == 'Floor'):
                    img = [(self.floor, pixel_coords)]
                elif(square.get_type() == 'Wall'):
                    img = [(self.wall, pixel_coords)]
                elif(square.get_type() == 'Item 1'):
                    img = [(self.floor, pixel_coords),
                           (self.needle, pixel_coords)]
                elif(square.get_type() == 'Item 2'):
                    img = [(self.floor, pixel_coords),
                           (self.plastic_tube, pixel_coords)]
                elif(square.get_type() == 'Item 3'):
                    img = [(self.floor, pixel_coords),
                           (self.syringe, pixel_coords)]
                elif(square.get_type() == 'Item 4'):
                    img = [(self.floor, pixel_coords),
                           (self.ether, pixel_coords)]
                elif(square.get_type() == 'Guard'):
                    img = [(self.floor, pixel_coords),
                           (self.guard, pixel_coords)]

                self.screen.blits(blit_sequence=img)

    def _draw_gyver(self):
        """
            private method : draw gyver and add the numbers of items he hold
        """
        pixel_coords = (self.PIXEL*Gyver.coords[0], self.PIXEL*Gyver.coords[1])

        # draw gyver
        self.screen.blit(self.gyver, pixel_coords)

        # draw number of items
        label = self.font_21.render(str(len(Gyver.items)), 1, (240, 0, 0))
        self.screen.blit(label, pixel_coords)

    def _draw_legend(self):
        legend = pygame.Surface((200, self.PIXEL*Labyrinth.rows))
        legend.fill((64, 0, 0))

        color = (240, 240, 240)

        num_items = str(len(Gyver.items))

        blits = [
            (
                self.font_21.render('Gyver Evasion', 1, color),
                (24, 16)
            ),
            (
                self.font_16.render(
                    'Number of items : ' + num_items + '/4',
                    1, color
                ),
                (26, 64)
            ),
        ]

        legend.blits(blit_sequence=blits)

        self.screen.blit(legend, (self.PIXEL*Labyrinth.columns, 0))

    def draw_labyrinth(self):
        self._draw_laby()
        self._draw_gyver()
        self._draw_legend()
        pygame.display.flip()

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

        win_screen = pygame.Surface(self.screen.get_size())
        win_screen.fill((255, 0, 0))

        win_screen.blit(self.font_21.render(
            'Congratulation !', 1, (240, 240, 240)), (290, 235))

        loop = True
        while loop:
            self.screen.blit(win_screen, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    loop = False

        print('Well Done !')

    def lose_scenario(self):

        lose_screen = pygame.Surface(self.screen.get_size())
        lose_screen.fill((255, 0, 0))

        lose_screen.blit(self.font_21.render(
            'Game Over...', 1, (240, 240, 240)), (290, 235))

        loop = True
        while loop:
            self.screen.blit(lose_screen, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    loop = False

        print('Game Over...')
