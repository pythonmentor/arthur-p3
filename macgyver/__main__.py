import os

from .gyver import Gyver
from .labyrinth import Labyrinth
from .gameloop import GameLoop
from .driver import TerminalDriver

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    Gyver.init_gyver({'x': 8, 'y': 4})
    Labyrinth.build_labyrinth()

    gameLoop = GameLoop(driver=TerminalDriver())

    gameLoop.start_loop()
    #gameLoop.end_game()

    return 0

if(__name__ == "__main__"):
    main()
