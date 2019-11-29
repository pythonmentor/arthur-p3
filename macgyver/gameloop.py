import os
import sys
import pygame

from .gyver import Gyver
from .labyrinth import Labyrinth

class GameLoop:
    """
        GameLoop is the loop of the laby game. If self.loop is equal to 1, the
        game is running.
    """

    TERMINAL = 'TERMINAL'
    PYGAME = 'PYGAME'

    WIN = "WIN"


    def __init__(self, **kwargs):
        self.loop = 0
        self.mode = kwargs.pop('mode', self.TERMINAL)

    def print_game(self):
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

    def draw_labyrinth(self):
        if(self.mode == self.TERMINAL):
            self.print_game()


    def wait_for_move(self):
        if(self.mode == self.TERMINAL):
            move = input('L, R, U, D (or QUIT) :\n')

        return move

    def perform_move(self, move):
        square = Labyrinth.get_square(Gyver.coords)

        if(move == 'R'):
            square = Gyver.move(x=1)
        elif(move == 'L'):
            square = Gyver.move(x=-1)
        elif(move == 'U'):
            square = Gyver.move(y=-1)
        elif(move == 'D'):
            square = Gyver.move(y=1)

        square.after_move(gyver=Gyver())

        # end conditions
        if(move == 'QUIT'):
            self.loop = 0
        if(Gyver.win):
            self.loop = 2


    def win_scenario(self):
        if(self.mode == self.TERMINAL):
            print("Well done !")


    def start_loop(self):
        self.loop = 1

        while self.loop == 1:
            self.draw_labyrinth()
            move = self.wait_for_move()
            self.perform_move(move)

        if(self.loop == 2):
            self.win_scenario()
