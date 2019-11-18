import os
from gyver import Gyver
from labyrinth import Labyrinth
from gameloop import GameLoop

ROOT_DIR = os.path.abspath('..')
LABY_PATH = ROOT_DIR + '/laby.txt'
RES_DIR = ROOT_DIR + '/res'

gyver = Gyver(coords=[1, 2])
labyrinth = Labyrinth(path=LABY_PATH)

def __main__():
    gameLoop = GameLoop(gyver, labyrinth)
    #gameLoop.startLoop()
    #gameLoop.endGame()
    return 0

if(__name__ == "__main__"):
    __main__()
