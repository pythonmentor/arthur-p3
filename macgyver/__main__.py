import os

from .gyver import Gyver
from .labyrinth import Labyrinth
from .gameloop import GameLoop
from .drivers import TerminalDriver, PygameDriver

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    gyver_coords = Labyrinth.build_labyrinth()
    Gyver.init_gyver(gyver_coords)

    #gameLoop = GameLoop(driver=TerminalDriver())
    gameLoop = GameLoop(driver=PygameDriver(30))

    gameLoop.start_loop()
    # gameLoop.end_game()

    return 0


if(__name__ == "__main__"):
    main()
