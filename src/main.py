#!venv/bin/python3.5 # -tc- je ne compterais pas sur le shebang pour le lancement ici

import os # -tc- ajouter une ligne vide après les imports standards
from gyver import Gyver
from labyrinth import Labyrinth
from gameloop import GameLoop

# -tc- Si tu lances le programme correctement, le
# -tc- ROOT_DIR sera le répertoire courant. Dans le doute,
# -tc- tu peux utiliser os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -tc- pathlib permet une syntaxe plus clair et est le module recommandé
ROOT_DIR = os.path.abspath('..')
RES_DIR = ROOT_DIR + '/res'

gyver = Gyver(coords=[1, 2])
labyrinth = Labyrinth()

# -tc- le fichier est habituellement appelé __main__.py, mais le point
# -tc- d'entrée est généralement appelé main()
def __main__():
    gameLoop = GameLoop(gyver, labyrinth)
    #gameLoop.startLoop()
    #gameLoop.endGame()
    return 0

if(__name__ == "__main__"):
    __main__()
