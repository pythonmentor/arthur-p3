#!/bin/bash

# -tc- Pas portable, éviter de lancer un scipt python avec un script bash. D'autant que ce 
# -tc- n'est pas nécessaire. Un script python aussi peut avoir un shebang

# -tc- Créer un package python avec un fichier __init__.py plutôt qu'un répertoire src (à moins
# -tc- d'avoir un setup.py ou pyproject.toml pour permettre l'installation dans l'environnement
# -tc- virtuel. Lancer le programme avec python -m macgyver si le package s'appelle mavcgyver
# -tc- et que le fichier de lancement s'appelle __main__.py

./src/main.py
