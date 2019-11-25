import os
import sys
import pygame

class GameLoop():
    """docstring for GameLoop."""

    gyver = None
    labyrinth = None

    def __init__(self, gyver, labyrinth, **kwargs):
        self.gyver = gyver
        self.labyrinth = labyrinth

        self.print_game()

        self.init_pygame()
        self.draw_labyrinth()

    def print_game(self):
        maps = self.labyrinth.maps

        for row in maps:
            s = ''
            for square in row:
                if(self.gyver.coords == square.coords):
                    s += '\t' + 'Gyver'
                else:
                    s += '\t' +  square.type

            print(s)

    def init_pygame(self):
        pygame.init()

        size = width, height = 700, 500
        screen = pygame.display.set_mode(size)

    def draw_labyrinth(self):
        print('draw labyrinth')


    def start_loop(self):
        gyverImg = pygame.image.load("res/MacGyver.png")
        gyverRect = gyverImg.get_rect().clip(pygame.Rect((0, 0), (50, 50)))

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
