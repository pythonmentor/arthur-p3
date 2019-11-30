import os
import sys
import pygame

from .gyver import Gyver
from .labyrinth import Labyrinth

from .drivers import Driver

class GameLoop:
    """
        GameLoop is the loop of the laby game.
        The self.loop value says :
        - 0 : stop
        - 1 : loop running
        - 2 : win
        - 3 : lose
        - 4 : pause
    """


    def __init__(self, **kwargs):
        self.loop = 0
        self.driver = kwargs.pop('driver', Driver)

    def perform_move(self, move):
        """
            Take a String and move MacGyver.
            The move value :
            - R : Right
            - L : Left
            - U : Up
            - D : Down
            - QUIT : Quit
        """

        if(move in ['R', 'L', 'U', 'D']):

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


    def start_loop(self):
        """
            The loop call only the driver and perform the move.
        """

        self.loop = 1

        while self.loop == 1:
            self.driver.draw_labyrinth()
            move = self.driver.wait_for_move()

            self.perform_move(move)

        if(self.loop == 2):
            self.driver.win_scenario()

        if(self.loop == 3):
            self.driver.lose_scenario()
