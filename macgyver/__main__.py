import os

from gyver import Gyver
from labyrinth import Labyrinth
from gameloop import GameLoop

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    gyver = Gyver(coords=[1, 2])
    labyrinth = Labyrinth()

    gameLoop = GameLoop(gyver, labyrinth)

    gameLoop.start_loop()
    #gameLoop.end_game()

    return 0

if(__name__ == "__main__"):
    main()
