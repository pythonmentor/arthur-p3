# Commentaires

Voici quelques commentaires en vrac sur la finalisation du jeu de MacGyver:
- Essaie d'étoffer ton README.md et, dans l'idéal, de le rédiger en anglais (bonne pratique sur github). Dans ce README, tu pourras donner une description de ton programme, ainsi que les instructions d'installation et de lancement. Ne pas oublier l'environnement virtuel.
- Dans ton Pipfile, la version de python est forcée à python 3.6. Il faudra donner les instructions dans ton README spécifiant que ton programme doit être utilisé avec python 3.6, ce qui est une version plus ancienne probablement que celle que la plupart des mentors utilisent par défaut. Ubuntu et Debian sont aujourd'hui passés à python 3.7 et la plupart des utilisateurs sous macos ou windows sont en python 3.7.
- La commande flake8 me retourne de nombreux points à corriger du point de vue de la PEP8. Tu peux installer flake8 à l'aide de la commande `pipenv install flake8 --dev` et exécuter la commande `flake8` à la racine de ton projet. Une partie des points à corriger sont des imports non utilisés (donc à éliminer).
- Si tu installes autopep8 à l'aide de la commande `pipenv install autopep8 --dev`, la commande `autopep8 --recursive --in-place .` à la racine de ton projet peut corriger la plupart des problèmes.
- Ajouter une docstring au début de la fonction main().
- Si tu installes et exécutes le programme pydocstyle à la racine de ton projet, tu verras que tes docstrings ne sont pas conforme à la [PEP257]](https://www.python.org/dev/peps/pep-0257/). Tu peux les corriger automatiquement en installant `pipenv install docformatter --dev`, puis en exécutant la commande `docformatter --recursive --in-place .` à la racine de ton projet. De cette manière, tu t'assure que tes docstrings sont toutes bien formatées. 
- Ta classe Labyrinth devrait utiliser des attributs d'instance et être instanciée. Par ailleurs, la manière avec laquelle tu définis et utilise tes méthodes statiques est incorrecte. Mais une telle pratique, dans le contexte de ce projet, n'est pas très objet.
- gameloop.py, ligne 37: square = Labyrinth.get_square(Gyver.coords) n'est pas très objet. Tu utilise une logique très procédurale qui pourrait t'être reprochée en soutenance. Gyver doit servir à instancier un objet représant ton héro. Ensuite, cet objet peut être utilisé comme un tout et passé par exemple en arguments de ta méthode get_square en entier get_square(macgyver). Dans un programme orienté-objet, il n'y a pas lieu de ne passer en argument d'une fonction qu'une partie d'un objet, comme ici l'attribut coords.

En résumé, Gyver et Labyrinth sont à transformer pour définir des instances et ensuite pouvoir manipuler tes instances comme des tout.

Sinon, le reste du programme est ok. Evite les constructions comme ici:
```python
if(move == 'QUIT'):
    self.loop = 0
if(Gyver.win):
    self.loop = 2
if(Gyver.lose):
    self.loop = 3
```
On ne sait pas ce que signifie 0, 2, 3. Utilise des constantes au nom descriptif (en majuscules) pour faciliter la lecture.

Dans le morceau de code ci-dessous:
```python
self.loop = 1

while self.loop == 1:
```
C'est pareil. Ce n'est pas très lisible. Je renommerais également self.loop en self.loop_status, plus descriptif à mon avis de ton intention.
