import os
import sys
import pygame

from .gyver import Gyver
from .labyrinth import Labyrinth

from .drivers import Driver

class GameLoop:
    """
        GameLoop is the loop of the laby game. If self.loop is equal to 1, the
        game is running.
    """

    WIN = "WIN"


    def __init__(self, **kwargs):
        self.loop = 0
        self.driver = kwargs.pop('driver', Driver)

    def draw_labyrinth(self):
        self.driver.draw_labyrinth()


    def wait_for_move(self):
        move = self.driver.wait_for_move()
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
        if(Gyver.lose):
            self.loop = 3


    def win_scenario(self):
        self.driver.win_scenario()


    def lose_scenario(self):
        self.driver.lose_scenario()


    def start_loop(self):
        self.loop = 1

        while self.loop == 1:
            self.draw_labyrinth()
            move = self.wait_for_move()
            self.perform_move(move)

        if(self.loop == 2):
            self.win_scenario()

        if(self.loop == 3):
            self.lose_scenario()
